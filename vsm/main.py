"""
Main file
"""

# package
from vsm import Config
from vsm.command_line import Cli


def run() -> None:
    """
    Example function to execute through poetry scripts
    """
    cli = Cli()
    if cli.args.run:
        print("args.run")

    print(f"Pacakge: {Config.package()}")
    print(f"Version: {Config.version()}")
    print(f"Base dir: {Config.base_dir()}")
    print(f"Session dir: {Config.session_dir()}")
