# pylint: disable = attribute-defined-outside-init

'''
This module defines the ChangeLog class.
'''

from io import StringIO
from datetime import date
from pathlib import Path
import re


UNRELEASED = 'Unreleased'


class ChangeLog:
    '''
    This class provides the functionality for maintaining logs of
    notable changes in a software project.
    '''

    break_marker: str = '[Breaking]'
    chlog_filename: str = 'CHANGELOG.md'
    chlog_prolog: str = ''
    types_of_change: dict[str, str] = {
        'added': 'Added',
        'fixed': 'Fixed',
        'changed': 'Changed',
        'deprecated': 'Deprecated',
        'removed': 'Removed',
        'security': 'Security',
    }
    date_mask = '%DATE%'
    use_brackets = False

    # @classmethod
    # @property
    # def group_names(cls) -> list[str]:
    #     '''Returns the supported group/section names.'''
    #     return [k for k in cls.types_of_change]

    @property
    def contains_changes(self) -> bool:
        '''
        Checks if the log contains any changes at all.
        '''
        num_changes = 0
        for change_type in self._unreleased_items:
            num_changes += len(self._unreleased_items[change_type])
        return num_changes > 0

    @property
    def contains_breaking_changes(self) -> bool:
        '''
        Checks if the log contains breaking changes.
        '''
        for change_type in ['break', 'breaks', 'breaking', 'removed']:
            change_notes = self._unreleased_items.get(change_type) or []
            if len(change_notes) > 0:
                return True
        for change_type in self._unreleased_items:
            for note in self._unreleased_items[change_type]:
                if note.startswith(f'- {ChangeLog.break_marker}'):
                    return True
        return False

    @property
    def current_version(self) -> str:
        '''Returns the current version of the changelog.'''
        return self.versions[0] if self.versions else None

    @property
    def prolog(self) -> str:
        '''
        Returns the changelog prolog. Prolog refers to the changelog
        text before the first version i.e. the first line starting
        with a "##". The prolog of an existing changelog file will
        never be altered by this ChangeLog class.
        '''
        return self._prolog

    @property
    def epilog(self) -> str:
        '''
        Returns the changelog epilog. Epilog refers to all text below
        the ## Unreleased section. The epilog of an exisiting changelog
        file will never be altered by this ChangeLog class.
        '''
        return self._epilog

    @property
    def versions(self) -> list[str]:
        '''
        Returns the software versions found in the changelog file.
        '''
        return self._versions

    def __init__(self):
        self.reset()

    def add(self, group: str, change_note: str, breaking=False) -> None:
        '''
        Adds a change note to the log.
        '''
        if group not in ChangeLog.types_of_change:
            raise ValueError(f'Invalid change type category "{group}"')
        change_note = (f'{ChangeLog.break_marker} {change_note}'
                       if breaking else change_note)
        self._unreleased_items[group].append(f'- {change_note}')
        self._numchanges += 1

    def freeze(self, version: str):
        '''
        Freezes the unreleased change notes by applying a version number.
        '''
        today = date.today().isoformat()
        date_str = self.date_mask.replace('%DATE%', today)
        self._unreleased_header = self._unreleased_header.replace(
            UNRELEASED, f'{version}'
        ).rstrip()
        self._unreleased_header += f' {date_str}\n\n'
        self._numchanges += 1

    def get(self, group: str) -> str:
        '''
        Returns the change notes in the group <group>
        '''
        if group not in ChangeLog.types_of_change:
            raise ValueError(f'Invalid change type category "{group}"')
        return '\n'.join(self._unreleased_items[group])

    def ingest(self, filename: str = None) -> None:
        '''
        Loads the changelog from the file indicated. Stores everything
        above the Unreleased section and everything below it in memory.
        Extracts the Unreleased section, if there is one.
        '''
        self.reset()
        self._clfile = Path(filename or ChangeLog.chlog_filename)
        if not self._clfile.exists():
            return
        raw = self._clfile.read_text(encoding='utf-8')
        versions = re.findall(r'^## (.+)', raw, flags=re.MULTILINE)
        sections = list(re.finditer(r'^## .+$', raw, flags=re.M))
        if not sections:
            return  # empty changelog file
        # Store everything above the first "##" in the prolog.
        # Extract the "Unreleased" section if there is one. Then,
        # store the remaining contents of the change log a.k.a. the
        # epilog.
        self._prolog = raw[0:sections[0].start()]
        next_index = sections[1].start() if len(sections) > 1 else None
        if UNRELEASED in versions[0]:
            # Convert the "Unreleased" section into a dict and discard the
            # original section.
            unreleased = raw[sections[0].start():next_index]
            self._unreleased_header, self._unreleased_items = (
                self._ingest_section(unreleased)
            )
            versions.pop(0)
            sections.pop(0)
        self._versions = versions
        self._epilog = raw[sections[0].start():] if versions else None

    def reset(self):
        '''
        Applies the factory defaults.
        '''
        self._clfile = Path(ChangeLog.chlog_filename)
        self._prolog = ''
        self._epilog = ''
        title = f'[{UNRELEASED}]' if ChangeLog.use_brackets else UNRELEASED
        self._unreleased_header = f'## {title}\n'
        self._unreleased_items = {k: [] for k in ChangeLog.types_of_change}
        self._versions = []
        self._numchanges = 0

    def save(self, filename: str = None) -> None:
        '''
        If no filename is given the original changelog will be
        overwritten only if some change notes have been added to the
        unreleased section via add(). If there are no new change notes
        there is nothing to save here.
        If a filename is given which is different from the file that was
        ingested then filename will be written to whether there are new
        change notes or not.
        '''
        # found = [kind for kind in self._unreleased]
        logfile = Path(filename) if filename else self._clfile
        if logfile == self._clfile and self._numchanges == 0:
            return
        with open(logfile, 'w', encoding='utf-8') as log:
            logtext = str(self)   # self.__str__()
            log.write(logtext)   # log.write(str(self))
        self._numchanges = 0

    def _format_unreleased_section(self):
        with StringIO() as clog:
            clog.write(self._unreleased_header)
            if not self._unreleased_header.endswith('\n\n'):
                # This means that this section is new in this changelog.
                # We need to insert another newline.
                clog.write('\n')
                # When this section is ingested the next time the newl;ine
                # will alreadt be there.
            for group in self._unreleased_items:
                if not self._unreleased_items[group]:
                    # No messages to store so leave the whole section out.
                    continue
                title = ChangeLog.types_of_change.get(group) or group
                clog.write(f'### {title}\n\n')
                for message in self._unreleased_items[group]:
                    clog.write(f'{message}\n')
                clog.write('\n')
            logtext = clog.getvalue().rstrip()
        return logtext

    @staticmethod
    def _get_key_by_value(value):
        for key, val in ChangeLog.types_of_change.items():
            if val == value:
                return key
        return None

    def _has_unreleased_items(self) -> bool:
        for kind in self._unreleased_items:
            if self._unreleased_items[kind]:
                return True
        return False

    @staticmethod
    def _ingest_section(text: str) -> tuple[str, list[str]]:
        # Implementation notes:
        # The text starts at the beginning of the ## Unreleased section and
        # ends just before the start of the next H2 heading. The regular
        # expressions find the H3 subsection titles (such as Added and Changed)
        # and the change items in each subsection. Those are stored in the
        # section items. When ingesting a changelog with unknown H3
        # subsections (e.g. New Features instead of Added), those will be
        # appended to the regular section_items. If we did not do this,
        # those unknown subsections would be lost when the changelog is
        # saved.
        if not text:
            return None, None
        titles = re.findall(r'^### (.+)', text, flags=re.MULTILINE)
        sections = list(m for m in re.finditer(r'^### .+$', text, flags=re.M))
        section_title = text[0:sections[0].start()]
        section_items = {k: [] for k in ChangeLog.types_of_change}
        undef_items = {}    # To pick up sections that are undefined in
                            # ChangeLog.types_of_change.   # noqa: E116
        titles.reverse()
        sections.reverse()   # To make the indexing, below, easier.
        last_index = None
        for title, section in zip(titles, sections):
            items = text[section.end():last_index]
            last_index = section.start()
            change_id = ChangeLog._get_key_by_value(title)
            if change_id not in section_items:
                undef_items[title] = []
                undef_items[title].append(items.strip())
                continue
            section_items[change_id].append(items.strip())
        # If there are undefined items, append them.
        undef_items = dict(reversed(undef_items.items()))
        for key, val in undef_items.items():
            section_items[key] = val
        return section_title, section_items

    def __str__(self):
        with StringIO() as clog:
            self._prolog = self._prolog or f'{ChangeLog.chlog_prolog}\n'
            clog.write(self._prolog)
            if self._has_unreleased_items():
                clog.write(self._format_unreleased_section())
                clog.write('\n')
                if self._epilog:
                    clog.write('\n')
            if self._epilog:
                clog.write(self._epilog)
            logtext = clog.getvalue()
        return logtext
