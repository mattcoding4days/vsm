"""
command line arguments for this app
"""

import argparse

from kickstart import ThreadSafeMeta


class Cli(metaclass=ThreadSafeMeta):
    """
    @description: App specific aruments go here
    """

    def __init__(self):
        self.__parser = argparse.ArgumentParser(
            prog="kickstart",
            usage="%(prog)s [options]",
            description="Example package",
            allow_abbrev=False,
        )
        self.__parser.add_argument(
            "-r",
            "--run",
            action="store_true"
        )

        # add more arguments here
        self.args = self.__parser.parse_args()
