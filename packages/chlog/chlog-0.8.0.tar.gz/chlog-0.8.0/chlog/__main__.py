#!/usr/bin/env python3
# pylint: disable=invalid-name

'''
Produces changelogs based on
https://keepachangelog.com/en/1.0.0/
and
https://semver.org/spec/v2.0.0.html.
'''

from argparse import ArgumentParser
from pathlib import Path

from InquirerPy import inquirer
from rich.markdown import Markdown

from . import cli_commands
from .changelog import ChangeLog
from .console import console
from .versioning import Versioning


def configure_cli():
    '''Configures the command line arguments and options'''
    mainparser = ArgumentParser(
        description=__doc__,
    )
    mainparser.add_argument(
        '-v', '--version',
        action='store_true',
        help='print the chlog version and exit',
    )
    command_title = console.swrite('[b]COMMAND[/]')
    command_help  = console.swrite('------- [b]command help[/]')
    subparsers = mainparser.add_subparsers(metavar=command_title,
                                           dest='command',
                                           help=command_help)
    for change_type in cli_commands:
        cmd = subparsers.add_parser(
            name=change_type['command'],
            help=change_type['help'],
            aliases=change_type.get('aliases', []),
            description=change_type['description'],
        )
        has_breaking_option = change_type.get('breaking')
        if has_breaking_option:
            cmd.add_argument(
                '-b', '--breaking',
                action='store_true',
                default=False,
                help='mark this change as a breaking change'
            )
        cmd.add_argument('changenote',
                         type=str,
                         help='describes the software modification')
        cmd.set_defaults(func=on_add_changenote, group=change_type['command'])

    freeze_cmd = subparsers.add_parser(
        name='freeze',
        aliases=['tag'],
        description='Tags all unreleased changes with a version number.',
        help='turn the Unreleased section into a released version'
    )
    freeze_cmd.add_argument('version', nargs='?', type=str,
                            help='version number')
    freeze_cmd.set_defaults(func=on_freeze)
    show_cmd = subparsers.add_parser(
        name='print',
        description='Renders the changelog Markdown and displays it '
                    'in the terminal.',
        help='pretty-print the changelog'
    )
    show_cmd.set_defaults(func=on_print)
    versions_cmd = subparsers.add_parser(
        name='versions',
        description='Shows the versions contained in the CHANGELOG, and '
                    'the suggested version number for the next version.',
        help='show the versions in the changelog'
    )
    versions_cmd.set_defaults(func=on_versions)
    #
    return mainparser


def on_add_changenote(args):
    '''
    Runs the commands with the arugments and options selected by the user.
    '''
    cl = ChangeLog()
    cl.ingest()
    if hasattr(args, 'breaking'):
        cl.add(args.group, args.changenote, breaking=args.breaking)
    else:
        cl.add(args.group, args.changenote)
    cl.save()


def on_freeze(args):
    '''
    "Freezes" the change notes that have been added since the last version
    by assigning them a version number.
    '''
    cl = ChangeLog()
    cl.ingest()
    if not cl.contains_changes:
        raise SystemExit('There are no unreleased change notes.')
    has_breaks = cl.contains_breaking_changes
    has_features = len(cl.get('added')) > 0
    has_fixes = len(cl.get('fixed')) > 0
    versioning = Versioning(cl.current_version,
                            breaks=has_breaks,
                            features=has_features,
                            fixes=has_fixes)
    version = args.version
    if not version:
        version = versioning.next_version()
        answer = inquirer.confirm(
            message=f'Suggesting version {version} - OK?',
            default=True,
            long_instruction='======',
        ).execute()
        if not answer:
            version = None
    else:
        try:
            warning = versioning.check_version(version)
            if warning:
                console.warning(warning)
                answer = inquirer.confirm(
                    message=f'Apply version {version} anyway?',
                    default=False,
                    long_instruction='======',
                ).execute()
                if not answer:
                    version = None
        except ValueError as verr:
            version = None
            console.error(verr)
        except EOFError:
            version = None
    if version:
        cl.freeze(version)
        cl.save()
        console.print(f'Tagged the Unreleased section with version {version}.')


def on_print(_):
    '''
    Renders the changelog Markdown to the terminal.
    '''
    # cl = ChangeLog()
    # cl.ingest()
    # console.print(Markdown(str(cl)))
    console.print(Markdown(Path(ChangeLog.chlog_filename)
                           .read_text(encoding='utf-8')))


def on_versions(_):
    '''
    Print the versions contained in the log.
    '''
    cl = ChangeLog()
    cl.ingest()
    #if not cl.contains_changes:
    #    return
    for ver in cl.versions:
        console.print(ver)
    has_breaks = cl.contains_breaking_changes
    has_features = len(cl.get('added')) > 0
    has_fixes = len(cl.get('fixed')) > 0
    # print(f'{has_breaks=}')
    # print(f'{has_features=}')
    # print(f'{has_fixes=}')
    versioning = Versioning(cl.current_version,
                            breaks=has_breaks,
                            features=has_features,
                            fixes=has_fixes)
    console.print('Based on the content of the changelog, the next version '
                  f'number should be {versioning.next_version()}.')


def main():
    # pylint: disable=missing-function-docstring
    parser = configure_cli()
    args = parser.parse_args()
    if args.version:
        from . import __version__
        print(f'chlog {__version__}')
        return
    if not args.command:
        parser.print_help()
        return
    args.func(args)


if __name__ == "__main__":
    main()
