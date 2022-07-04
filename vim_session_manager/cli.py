"""
argparse wrapper
"""

import argparse

from vim_session_manager import ThreadSafeMeta, Config


class SubCommand:
    LIST: str = "list"
    REMOVE: str = "remove"
    OPEN: str = "open"


class Cli(metaclass=ThreadSafeMeta):
    """
     @description: App specific aruments go here
     """

    def __init__(self):
        parser = argparse.ArgumentParser(
            prog=f"{Config.executable()}",
            usage="%(prog)s [options]",
            description=f"""vsm v{Config.version()} is a small python program for easily loading/viewing and removing vim sessions
                                        as well as listing programmer statistics""",
            allow_abbrev=False,
        )
        subcommands = parser.add_subparsers(
            dest='command', help='Available commands')

        subcommands.add_parser(
            SubCommand.LIST, help="List all available vim session files in VIM_SESSIONS directory")

        remove_session_command = subcommands.add_parser(
            SubCommand.REMOVE, help="Remove session(s) by name or interactively")

        remove_session_command.add_argument("-n", "--name",
                                            help="Remove a vim session file by name", type=str)

        open_session_command = subcommands.add_parser(
            SubCommand.OPEN, help="Open a session by name or interactively")

        open_session_command.add_argument("-n", "--name",
                                          help="Open a vim session file by name", type=str)

        self.__args = parser.parse_args()

    @property
    def active_command(self) -> str:
        return self.__args.command

    @property
    def args(self) -> argparse.Namespace:
        """
        @description: Return the argparse object
        """
        return self.__args
