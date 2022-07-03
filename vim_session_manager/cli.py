"""
argparse wrapper
"""

import argparse

from vim_session_manager import ThreadSafeMeta, Config

# TODO: arguments (-l, -r, and -o) should be changed to subcommands


class Cli(metaclass=ThreadSafeMeta):
    """
     @description: App specific aruments go here
     """

    def __init__(self):
        parser = argparse.ArgumentParser(
            prog=f"{Config.executable()} {Config.version()}",
            usage="%(prog)s [options]",
            description="""A small python program for easily loading/viewing and removing vim sessions
                                        as well as listing programmer statistics""",
            allow_abbrev=False,
        )
        exclusive = parser.add_mutually_exclusive_group()

        exclusive.add_argument("-l", "--list-sessions",
                               help="show all vim session files in VIM_SESSIONS directory", action="store_true")
        exclusive.add_argument("-r", "--remove-session",
                               help="remove a vim session file by name", type=str)
        exclusive.add_argument("-o", "--open-session",
                               help="open a vim session file by name", type=str)

        self.__args = parser.parse_args()

    @property
    def args(self) -> argparse.Namespace:
        """
        @description: Return the argparse object
        """
        return self.__args
