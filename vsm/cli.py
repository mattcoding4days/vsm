"""
argparse wrapper
"""

import argparse

from vsm import ThreadSafeMeta


class Cli(metaclass=ThreadSafeMeta):
    """
     @description: App specific aruments go here
     """

    def __init__(self):
        parser = argparse.ArgumentParser(
            prog="vsm",
            usage="%(prog)s [options]",
            description="A small python program for easily loading/viewing and removing vim sessions",
            allow_abbrev=False,
        )
        parser.add_argument("-l", "--list-sessions",
                            help="show all vim session files in VIM_SESSIONS directory", action="store_true")
        parser.add_argument("-r", "--remove-session",
                            help="remove a vim session file by name", type=str)
        parser.add_argument("-o", "--open-session",
                            help="open a vim session file by name", type=str)
        parser.add_argument(
            "--the-current-state-of-things", help="show information about the current state of things", action="store_true")

        self.__args = parser.parse_args()

    @property
    def args(self) -> argparse.Namespace:
        """
        @description: Return the argparse object
        """
        return self.__args
