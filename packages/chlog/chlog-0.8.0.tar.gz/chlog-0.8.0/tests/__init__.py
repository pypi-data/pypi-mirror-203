
'''
Need a package for tests so loggenerator can be imported by the
test modules. Also sets the HOME enviroment to the directory which
contains this file. This is to avoid picking up ~/.config/chlog.toml
oe ./pyproject.toml.
'''

from pathlib import Path
import os


os.environ['HOME'] = str(Path(__file__).parent.resolve())
