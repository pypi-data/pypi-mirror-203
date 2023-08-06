# pylint: disable = too-few-public-methods

'''
Test cases for the command line interface.
'''

from pathlib import Path
import sys
from textwrap import dedent

from pybrownies.testing import tmpdir
import pytest
from rich.text import Text

from chlog import config
import chlog.__main__
from chlog.__main__ import main
from chlog.changelog import ChangeLog

from .loggenerator import LogGenerator


class ExecutorMock:
    '''
    Mimic the InquirerPySessionResult return by various
    InquirerPy.inquirer methods.
    '''
    def __init__(self, return_value):
        self._return_value = return_value

    def execute(self):
        # pylint: disable = missing-function-docstring
        return self._return_value


class InquirerMock:
    '''
    Mimic various interactive InquirerPy prompts in
    meche.__main__.get_settings().
    '''
    def confirm(self, message, default, **kwargs):
        # pylint: disable = missing-function-docstring, unused-argument
        return ExecutorMock(default)


chlog.__main__.inquirer = InquirerMock()


@tmpdir
def test_add_changenote():
    '''
    Verify that change notes are correctly added to the changelog.
    '''
    sys.argv = ['chlog', 'added', 'Test message.']
    main()
    sys.argv = ['chlog', 'changed', '--breaking', 'Test message.']
    main()
    changelog = Path('CHANGELOG.md')
    assert changelog.exists()
    content = changelog.read_text(encoding='utf-8')
    assert '### Added' in content
    assert '### Changed' in content
    assert 'Test message.' in content
    assert f'{config.breaking_prefix}' in content


@tmpdir
def test_freeze(capsys):
    # pylint: disable = invalid-name
    '''
    Verify that ChangeLog.freeze applies version numbers correctly.
    '''
    lg = LogGenerator('CHANGELOG', numlines_between_sections=1)
    lg.make_full_log()
    sys.argv = ['chlog', 'freeze']
    main()
    cl = ChangeLog()
    cl.ingest()
    assert len(cl.versions) == 3
    assert cl.versions[0].startswith('0.7.0')
    out, _ = capsys.readouterr()
    plain = Text.from_ansi(out).plain
    assert 'Tagged the Unreleased section with version 0.7.0.' in plain
    # Now check that freeze abends if the Unreleased section is empty.
    markdown = '''
    # Changelog

    This file contains bla bla.

    ## 1.0.0 - 2022-02-22

    ### Added

    - One lonely feature.
    '''
    Path('CHANGELOG.md').write_text(markdown, encoding='utf-8')
    with pytest.raises(SystemExit):
        sys.argv = ['chlog', 'freeze']
        main()


@tmpdir
def test_versions(capsys):
    Path('CHANGELOG.md').touch()
    sys.argv = ['chlog', 'versions']
    main()
    out, _ = capsys.readouterr()
    plain = Text.from_ansi(out).plain
    assert '0.1.0' in plain
    markdown = '''
    # Changelog

    This file contains bla bla.

    ## 1.0.0 - 2022-02-22

    ### Added

    - One lonely feature.
    '''
    Path('CHANGELOG.md').write_text(dedent(markdown), encoding='utf-8')
    main()
    out, _ = capsys.readouterr()
    plain = Text.from_ansi(out).plain
    assert '1.1.0' in plain
    markdown = '''
    # Changelog

    This file contains bla bla.

    ## Unreleased

    ### Fixed

    - Fixed the pesky foo bug.

    ## 1.0.0 - 2022-02-22

    ### Added

    - One lonely feature.

    ## 0.9.0 - 2022-02-22

    ### Added

    - One lonely feature.
    '''
    Path('CHANGELOG.md').write_text(dedent(markdown), encoding='utf-8')
    main()
    out, _ = capsys.readouterr()
    plain = Text.from_ansi(out).plain
    for ver in ['0.9.0', '1.0.0', '1.0.1']:
        assert ver in plain


def test_show_version(capsys):
    sys.argv = ['chlog', '--version']
    main()
    out, _ = capsys.readouterr()
    plain = Text.from_ansi(out).plain
    from chlog import __version__
    assert plain == f'chlog {__version__}'
