
'''
Manage the chlog tool's configuration.
'''

from copy import deepcopy
from dataclasses import dataclass, field
from pathlib import Path
from textwrap import dedent
try:
    from tomllib import load as load_toml
except ModuleNotFoundError:
    from tomli import load as load_toml


@dataclass
class Config:
    '''
    Loads configuration settings from TOML files.
    '''
    breaking_prefix: str = None   # Prefix that indicates a breaking change
    # Command definitions for the chlog app:
    chlog_commands: list[dict] = field(default_factory=list)
    chlog_filename: str = None   # The changelog file name
    chlog_prolog: str = None   # The text to begin the changelog with
    # A dictionary which maps change_types such as "added" to their
    # labels e.g. "New features":
    types_of_change: dict[str, str] = field(default_factory=dict)
    use_brackets: bool = False

    def __post_init__(self):
        '''
        Initialize the default settings from the TOML file defaults.toml.
        '''
        toml_path = Path(__file__).parent.resolve() / 'defaults.toml'
        with open(toml_path, 'rb') as fp:
            config = load_toml(fp)
        settings = config['tool']['chlog']
        self.breaking_prefix = settings.get('break-marker')
        self.chlog_commands = deepcopy(settings['commands'])
        self.chlog_filename = settings.get('chlog-filename')
        self.chlog_prolog = dedent(settings.get('chlog-prolog'))
        self.date_mask = settings.get('date-mask')
        self.use_brackets = settings.get('use-brackets')
        self.__update_change_types()

    def merge_configs(self, filename: str = None):
        '''
        Merge the defaull settings with settings from other TOML files.
        If a file name argument is provided, the settings will be loaded
        from that file. Otherwise pyproject.toml will be loaded, if it
        exists. If not, and if ~/.config/chlog.toml exists, then that
        will be loaded. If no files are found at all, the default
        settings remain unchanged.
        '''
        this_toml = Path(filename) if filename else None
        prj1_toml = Path('pyproject.toml')
        prj2_toml = Path('chlog.toml')
        prj3_toml = Path('.chlog')
        home_toml = Path.home().resolve() / '.config' / 'chlog.toml'
        toml = {}
        for config_path in [this_toml,
                            prj1_toml, prj2_toml, prj3_toml,
                            home_toml]:
            if config_path and config_path.exists():
                with open(config_path, 'rb') as fp:
                    toml = load_toml(fp)
                break   # Stop after the first file found.
        tools = toml.get('tool')
        config = tools.get('chlog') if tools else None
        if not config:
            return
        self.breaking_prefix = config.get('break-marker', self.breaking_prefix)
        self.chlog_filename = config.get('chlog-filename', self.chlog_filename)
        commands = config.get('commands')
        if commands:
            self.__parse_commands(commands)
            self.__update_change_types()

    def __parse_commands(self, commands):
        for item in commands:
            assert 'command' in item
            found = [
                k for k in self.chlog_commands
                if k['command'] == item['command']
            ]
            elem = found[0] if found else {}
            if not found:
                insert_pos = item.get('insert-before')
                if insert_pos:
                    self.chlog_commands.insert(insert_pos, elem)
                else:
                    self.chlog_commands.append(elem)
            for key in item:
                elem[key] = item[key]

    def __update_change_types(self):
        h3_titles = [k['heading'] for k in self.chlog_commands]
        h3_types = [k['command'] for k in self.chlog_commands]
        self.types_of_change = dict(zip(h3_types, h3_titles))


def get_config_by_name(config_name):
    '''
    LOads the named cobfiguration from
    <site-packages>/chlog/config/<config_name>.toml
    '''
    toml_path = Path(__file__).parent.resolve() / f'{config_name}.toml'
    cfg = Config()
    cfg.merge_configs(str(toml_path))
    return cfg
