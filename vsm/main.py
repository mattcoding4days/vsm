"""
Main file
"""

# standard lib
import sys

# package
from vsm import Config
from vsm.session_manager import VimSessionManager
from vsm.cli import Cli
from vsm.log import Log


def main():
    """
    @description: executor function
    """
    cli = Cli()
    vsm = VimSessionManager()
    if cli.args.list_sessions:
        vsm.list_sessions()

    elif cli.args.remove_session:
        Log.info(f"remove session command called: {cli.args.remove_session}")

    elif cli.args.open_session:
        Log.info(f"load session command called: {cli.args.open_session}")

    elif cli.args.the_current_state_of_things:
        Log.warn(f"This feature is currently under development")

    else:
        Log.error(
            f"No arguments give, please use `{Config.package()} --help` for usage information")
        sys.exit(1)


if __name__ == "__main__":
    main()
