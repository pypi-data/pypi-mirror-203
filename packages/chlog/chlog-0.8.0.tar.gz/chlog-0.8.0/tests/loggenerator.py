
'''
Generates changelog files which unit tests must be able to reproduce.
'''

from textwrap import dedent
from chlog import config
from chlog.changelog import UNRELEASED


class LogGenerator:
    '''
    Generates changelog files which unit tests must be able to reproduce.
    '''
    def __init__(self, testcase_name: str, numlines_between_sections: int):
        self._numlines_between_sections = '\n' * numlines_between_sections
        self._testcase_name = testcase_name
        self._changelog = ''

    def make_full_log(self, versions: list[str] = ['0.6.0', '0.5.0'],
                      filestem: str = None):
        # pylint: disable = dangerous-default-value
        '''
        Generates a changelog file which contains both an Unreleased
        section and sections. for released versions.
        '''
        logfile = filestem or self._testcase_name
        with open(f'{logfile}.md', 'w', encoding='utf-8') as fid:
            output = f'{config.chlog_prolog}{self._numlines_between_sections}'
            output += f'{self._generate_section_for_version(version=None)}'
            output += f'{self._numlines_between_sections}'
            for ver in versions:
                output += f'{self._generate_section_for_version(ver)}'
                output += f'{self._numlines_between_sections}'

            output = output.rstrip()
            fid.write(f'{output}\n')

    def make_released_only(self, versions: list[str] = ['0.6.0', '0.5.0'],
                           filestem: str = None):
        # pylint: disable = dangerous-default-value
        '''
        Generates a changelog file without an Unreleased section.
        '''
        logfile = filestem or self._testcase_name
        with open(f'{logfile}.md', 'w', encoding='utf-8') as fid:
            output = f'{config.chlog_prolog}{self._numlines_between_sections}'
            for ver in versions:
                output += f'{self._generate_section_for_version(ver)}'
                output += f'{self._numlines_between_sections}'

            output = output.rstrip()
            fid.write(f'{output}\n')

    def make_unreleased_only(self, filestem: str = None):
        '''
        Generates a changelog file which contains only an Unreleased
        section.
        '''
        logfile = filestem or self._testcase_name
        with open(f'{logfile}.md', 'w', encoding='utf-8') as fid:
            fid.write(config.chlog_prolog)
            fid.write(self._numlines_between_sections)
            output = self._generate_section_for_version(version=None).rstrip()
            fid.write(output)
            fid.write('\n')

    def _generate_section_for_version(self, version: str):
        title = version or UNRELEASED
        date = ' - 2022-02-02' if version else ''
        output = f'## {title}{date}\n\n'
        for title in ['Added', 'Fixed']:
            section = (
                f'### {title}\n'
                '\n'
                f'- {self._testcase_name}.\n'
                '- Another item.\n\n'
            )
            output += dedent(section)
        return output[:-1]
