'''
Keep changelogs the easy way

:copyright: (c) 2023 Ralf Luetkemeier
:license: MIT, see LICENSE for more details.
'''

from copy import deepcopy

from .changelog import ChangeLog
from .config import Config


__version__ = "0.8.0"


config = Config()
config.merge_configs()
ChangeLog.break_marker = config.breaking_prefix
ChangeLog.chlog_filename = config.chlog_filename
ChangeLog.chlog_prolog = config.chlog_prolog
ChangeLog.types_of_change = deepcopy(config.types_of_change)
ChangeLog.date_mask = deepcopy(config.date_mask)
ChangeLog.use_brackets = config.use_brackets
cli_commands = config.chlog_commands
