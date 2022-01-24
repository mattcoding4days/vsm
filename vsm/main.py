"""
Main file
"""

# standard lib

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
        Log.info("remove session command called")

    elif cli.args.load_session:
        Log.info("load session command called")

    else:
        Log.error(f"No arguments give, please use {Config.package()} --help for usage information")

if __name__ == "__main__":
    main()