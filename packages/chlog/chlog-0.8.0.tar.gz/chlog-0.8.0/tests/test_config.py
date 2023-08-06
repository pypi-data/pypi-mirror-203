
'''
Test cases for the Config class.
'''

import os
from pathlib import Path
from platform import uname
from textwrap import dedent

from pybrownies.testing import tmpdir

from chlog.config import Config


def test_init():
    '''
    Verify that instances of Config are created with the expected default
    settings.
    '''
    cfg = Config()
    assert cfg.breaking_prefix == '[Breaking]'
    assert cfg.chlog_filename == 'CHANGELOG.md'
    assert len(cfg.chlog_commands) == 6
    assert len(cfg.types_of_change.keys()) == 6


@tmpdir
def test_merge():
    '''
    Verify that settings loaded from an additional TOML config file
    correctly overwrite the respective default setting, and that new
    settings are created correctly as well.
    '''
    toml = '''
        [tool.chlog]
        break-marker = "BREAK:"

        [[tool.chlog.commands]]
        command = "added"
        heading = "New Features"

        [[tool.chlog.commands]]
        command = "improved"
        heading = "Improved"
        help = "adds an improvement note to the changelog"
        description="Records improvements in the changelog."
        insert-before = 1
    '''
    with open('test.toml', 'w', encoding='utf-8') as fp:
        fp.write(dedent(toml))
    cfg = Config()
    cfg.merge_configs('test.toml')
    assert cfg.breaking_prefix == 'BREAK:'
    assert cfg.chlog_filename == 'CHANGELOG.md'
    assert len(cfg.chlog_commands) == 7
    assert cfg.types_of_change['added'] == 'New Features'
    assert cfg.types_of_change['fixed'] == 'Fixed'
    assert cfg.types_of_change['improved'] == 'Improved'


@tmpdir
def test_load_order():
    '''
    Verify that Config picks up ~/.config/chlog.toml, if there is one.
    '''
    varname = 'HOME' if uname().system != 'Windows' else 'USERPROFILE'
    home = os.environ[varname]
    try:
        # Verify that Config picks up ~/.config/chlog.toml, if there is one.
        toml = '''
            [tool.chlog]
            chlog-filename = "chlog-test.toml"
        '''
        cfg = Config()
        cfg.merge_configs()
        assert cfg.chlog_filename == 'CHANGELOG.md'   # i.e. unchanged
        cfgdir = Path('.config')
        cfgdir.mkdir()
        with open(cfgdir / 'chlog.toml', 'w', encoding='utf-8') as fp:
            fp.write(dedent(toml))
        os.environ[varname] = str(Path().cwd().resolve())
        cfg = Config()
        cfg.merge_configs()
        assert cfg.chlog_filename == 'chlog-test.toml'
        # Create a pyproject.toml here and verify that Config loads
        # that instead.
        toml = '''
            [tool.chlog]
            chlog-filename = "pyproject.toml"
        '''
        with open('pyproject.toml', 'w', encoding='utf-8') as fp:
            fp.write(dedent(toml))
        cfg = Config()
        cfg.merge_configs()
        assert cfg.chlog_filename == 'pyproject.toml'
    finally:
        os.environ[varname] = home
