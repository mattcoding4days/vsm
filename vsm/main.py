"""
Main file
"""

# standard lib
import sys

# package
from vsm import Config
from vsm.cli import Cli
from vsm.log import Log

def main():
    """
    @description executor function
    """
    cli = Cli()
    if cli.args.list_sessions:
        Log.info("list sessions command called")

    elif cli.args.remove_session:
        Log.info(f"remove session command called: {cli.args.remove_session}")

    elif cli.args.load_session:
        Log.info(f"load session command called: {cli.args.load_session}")

    else:
        Log.error(f"No arguments give, please use `{Config.package()} --help` for usage information")
        sys.exit(1)

if __name__ == "__main__":
    main()