
'''
Support for validating version numbers
'''

import re
from semver import VersionInfo
# V3: from semver.version import Version


class Versioning:
    '''
    Suggests and validates semantic version numbers
    '''
    @property
    def current_version(self) -> str:
        '''Returns the current version of the changelog'''
        return self._current_version or '0.0.0'

    def __init__(self, current_version,
                 breaks: bool = False,
                 features: bool = False,
                 fixes: bool = False):
        self._current_version = None
        self._features = features
        self._fixes = fixes
        self._breaks = breaks
        if current_version:
            rex = re.compile(
                r'^[\D\(\[ ]*[\(\[]?(\d+\.\d+\.\d+[^ ]*)[\)\]]?.*$'
            )
            match = rex.search(current_version.strip())
            self._current_version = match.group(1).strip('[]()')

    def next_version(self, hint=None) -> str:
        '''
        Suggests a new version number based on the content of the log
        or the hint argument provided.
        '''
        valid_hints = ['major', 'minor', 'patch', 'prerelease']
        if hint and hint not in valid_hints:
            raise ValueError(f'must be one of {", ".join(valid_hints)}')
        if not self._current_version:
            return '0.1.0'
        ver = VersionInfo.parse(self._current_version)
        if ver.major == 0:
            self._breaks = False
        if hint == 'prerelease':
            return str(ver.next_version(part='prerelease'))
        if self._breaks or hint == 'major':
            return str(ver.next_version(part='major'))
        if self._features or hint == 'minor':
            return str(ver.next_version(part='minor'))
        if self._fixes or hint == 'patch':
            return str(ver.next_version(part='patch'))
        return str(ver.next_version(part='minor'))

    def check_version(self, version):
        '''
        Tests if the argument is a valid sematic version number. Returns
        a warning message if the argument is not a valid number. Raises
        a ValueError if the argument is malformatted.
        '''
        # Returns None if the version is valid.
        # Returns a warning message if the version number should be
        # different according to semantic version rules.
        # Raises a ValueError if the version cannot be parsed or if
        # it is the same or less than the current version.
        ver1 = VersionInfo.parse(version)
        ver2 = VersionInfo.parse(self.current_version)
        ver3 = VersionInfo.parse(self.next_version())
        if ver1 <= ver2:
            raise ValueError('The version must be higher than the '
                             f'current version {self.current_version}.')
        warning = None
        if self._breaks and ver1.major == ver2.major:
            warning = 'The change log contains breaking changes.\n' \
                     f'The next version should probably be {ver3}.'

        return warning
