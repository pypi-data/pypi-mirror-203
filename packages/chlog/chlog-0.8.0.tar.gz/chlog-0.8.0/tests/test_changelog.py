# pylint: disable = invalid-name, missing-function-docstring, protected-access

'''
Test cases for the Changelog class.
'''

from copy import deepcopy
from difflib import SequenceMatcher
from pathlib import Path
from textwrap import dedent

# import pytest

from pybrownies.testing import tmpdir

from chlog import config
from chlog.changelog import ChangeLog
from chlog.config import get_config_by_name

from .loggenerator import LogGenerator


# region: Verify that ChangeLog will not reformat existing log content.


@tmpdir
def test_in_equals_out():
    '''
    Read changelogs and save them without modifications. Verify that
    inputs and outputs are exactly the same.
    '''
    lg = LogGenerator('released-b', numlines_between_sections=1)
    lg.make_released_only()
    lg = LogGenerator('unreleased-b', numlines_between_sections=1)
    lg.make_unreleased_only()
    lg = LogGenerator('full-log-b', numlines_between_sections=1)
    lg.make_full_log()

    for filename in ['released', 'unreleased', 'full-log']:
        infile = f'{filename}-b.md'
        outfile = f'{filename}-a.md'
        content_before = Path(infile).read_text(encoding='utf-8')
        cl = ChangeLog()
        cl.ingest(infile)
        cl._numchanges = 1   # Ensure save() does not exit early.
        cl.save(outfile)
        content_after = Path(outfile).read_text(encoding='utf-8')
        assert len(content_before) == len(content_after)
        assert content_after == content_before


@tmpdir
def test_formatting_is_lossless():
    '''
    Ingest a changelog with unreleased and version sections. Add a
    single improvement. Verify that formmating of everything else
    remains intact.
    '''
    lg = LogGenerator('full-log', numlines_between_sections=1)
    lg.make_full_log()
    content_before = Path('full-log.md').read_text(encoding='utf-8')
    Path('full-log-before.md').write_text(content_before, encoding='utf-8')
    cl = ChangeLog()
    cl.ingest('full-log.md')
    cl.add('changed', 'A changed feature.')
    cl.save()
    content_after = Path('full-log.md').read_text(encoding='utf-8')
    assert len(content_before) != len(content_after)
    matcher = SequenceMatcher(a=content_before, b=content_after)
    blocks = matcher.get_matching_blocks()
    # See https://docs.python.org/3/library/difflib.html
    assert 3 == len(blocks)
    # The addition we were making is "### Improved\n\n- An improvement.\n\n\n".
    expected_diff = dedent('''
    ### Changed

    - A changed feature.

    ''')[1:]
    len_a, len_b, _ = blocks[2]
    assert len_b == len_a + len(expected_diff)
    # Block[1] describes the range of chars which is different.
    start_idx, end_idx, _ = blocks[1]
    # The difference seen by the matcher is
    # '''
    # ##"# Improved
    #
    # - An improvement.
    #
    # ##" 0.6.0 -
    # '''
    # which means that the indices must be adjusted like this
    start_idx -= 2
    end_idx -= 2
    # in order to the difference as expected by a human.
    assert content_after[start_idx:end_idx] == expected_diff
    # And since the matcher returned no more than 3 blocks, there are no
    # more differences.

# endregion

# region: Make sure ChangeLog handles empty log files.


@tmpdir
def test_ingest_nologfile():
    '''
    Verify that ChangeLog.ingest() will result in an empty changelog,
    without errors.
    '''
    cl = ChangeLog()
    cl.ingest()
    assert not cl.prolog
    assert not cl.epilog
    non_empty_sections = [v for v in cl._unreleased_items.values() if len(v)]
    assert not non_empty_sections


@tmpdir
def test_ingest_emptylogfile():
    '''
    Verify that loading a changelog file with no content will result
    in an empty changelog.
    '''
    with open('empty.md', 'w', encoding='utf-8') as fp:
        fp.write('')
    cl = ChangeLog()
    cl.ingest('empty.md')
    assert not cl.prolog
    assert not cl.epilog
    non_empty_sections = [v for v in cl._unreleased_items.values() if len(v)]
    assert len(non_empty_sections) == 0


@tmpdir
def test_start_new_changelog():
    cl = ChangeLog()
    cl.save()
    logfile = Path(cl.chlog_filename)
    assert not Path(logfile).exists()
    cl.add('added', 'New feature A.')
    cl.save()
    assert Path(logfile).exists()
    content = logfile.read_text(encoding='utf-8')
    assert content.startswith(config.chlog_prolog)
    assert '## Unreleased' in content or '## [Unreleased]' in content
    assert content.rstrip().endswith('New feature A.')

# endregion

# region: Verify that ChangeLog ingests different log files correctly.


@tmpdir
def test_ingest():
    lg = LogGenerator(None, numlines_between_sections=1)
    lg.make_full_log(filestem='full')
    lg = LogGenerator(None, numlines_between_sections=1)
    lg.make_released_only(filestem='released')
    lg = LogGenerator(None, numlines_between_sections=1)
    lg.make_unreleased_only(filestem='unreleased')
    cl_full = ChangeLog()
    cl_released = ChangeLog()
    cl_unreleased = ChangeLog()
    cl_full.ingest('full.md')
    cl_released.ingest('released.md')
    cl_unreleased.ingest('unreleased.md')
    assert cl_full.prolog.startswith(config.chlog_prolog)
    assert cl_full.epilog == cl_released.epilog
    # for kind in ChangeLog.group_names:
    #     assert len(cl_full.get(kind)) == len(cl_unreleased.get(kind))
    num_matches = 0
    for heading in cl_full.versions:
        if '0.5.0' in heading:
            num_matches += 1
        if '0.6.0' in heading:
            num_matches += 1
    assert num_matches == 2

# endregion

# region: Confirm that version handling is correct.


def test_contains_breaking_changes():
    cl = ChangeLog()
    cl.add('changed', 'A change.')
    assert not cl.contains_breaking_changes
    cl.add('changed', 'A breaking change.', breaking=True)
    assert cl.contains_breaking_changes
    cl = ChangeLog()
    cl.add('removed', 'A removal.')
    assert cl.contains_breaking_changes


@tmpdir
def test_versions():
    cl = ChangeLog()
    assert cl.current_version is None
    assert not cl.versions
    cl.add('fixed', 'A bug fix.')
    assert cl.current_version is None
    assert not cl.versions
    cl.freeze('0.2.0')
    cl.save()
    cl.ingest()
    assert '0.2.0' in cl.current_version


# endregion


@tmpdir
def test_alt_log():
    break_marker = ChangeLog.break_marker
    chlog_filename = ChangeLog.chlog_filename
    types_of_change = ChangeLog.types_of_change
    use_brackets = ChangeLog.use_brackets
    config = get_config_by_name('alternative')
    try:
        ChangeLog.break_marker = config.breaking_prefix
        ChangeLog.chlog_filename = config.chlog_filename
        ChangeLog.types_of_change = deepcopy(config.types_of_change)
        ChangeLog.use_brackets = False
        cl = ChangeLog()
        for kind in config.types_of_change:
            cl.add(kind, 'A change note.')
        cl.save()
        content = Path(ChangeLog.chlog_filename).read_text(encoding='utf-8')
        assert '## Unreleased' in content
        for h3 in ['New features', 'Improvements', 'Bug fixes',
                   'Breaking changes', 'Changes', 'Deprecations',
                   'Removed features', 'Security', 'Documentation']:
            assert f'### {h3}' in content
        cl = ChangeLog()
        cl.ingest()
        assert len(cl._unreleased_items) == 9
        content = '''
        # Changelog

        ## Unreleased

        ### Notable changes

        - Change 1.
        - Change 2.

        ### Important additions

        - Just this one.
        '''
        Path(ChangeLog.chlog_filename).write_text(dedent(content),
                                                  encoding='utf-8')
        cl = ChangeLog()
        cl.ingest()
        assert 'Notable changes' in cl._unreleased_items
        assert 'Important additions' in cl._unreleased_items
        assert len(cl._unreleased_items['Notable changes'][0].split('\n')) == 2
        assert len(cl._unreleased_items['Important additions']) == 1
        cl.add('added', 'An addition.')
        cl.save()
        content = Path(ChangeLog.chlog_filename).read_text(encoding='utf-8')
        assert 'New features' in content
        assert 'Notable changes' in content
        assert 'Important additions' in content
        cl = ChangeLog()
        cl.ingest()
        num_nonempty = 0
        for _, val in cl._unreleased_items.items():
            if val:
                num_nonempty += 1
        assert num_nonempty == 3
    finally:
        ChangeLog.break_marker = break_marker
        ChangeLog.chlog_filename = chlog_filename
        ChangeLog.types_of_change = types_of_change
        ChangeLog.use_brackets = use_brackets


@tmpdir
def test_brackets():
    use_brackets = ChangeLog.use_brackets
    try:
        ChangeLog.use_brackets = True
        cl = ChangeLog()
        for kind in ChangeLog.types_of_change:
            cl.add(kind, 'A change note.')
        cl.save()
        content = Path(ChangeLog.chlog_filename).read_text(encoding='utf-8')
        assert '## [Unreleased]' in content
        cl.freeze('0.3.0')
        cl.save()
        content = Path(ChangeLog.chlog_filename).read_text(encoding='utf-8')
        assert '## [0.3.0]' in content
    finally:
        ChangeLog.use_brackets = use_brackets
