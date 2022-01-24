"""
Main file
"""

# standard lib

# package
from vsm import Config
from vsm.command_line import Cli
from vsm.log import Log


def run() -> None:
    """
    Example function to execute through poetry scripts
    """
    cli = Cli()
    if cli.args.run:
        Log.info(f"-r was passed")

    Log.info(f"Pacakge: {Config.package()}")
    Log.info(f"Version: {Config.version()}")
    Log.info(f"Base dir: {Config.base_dir()}")
    Log.info(f"Config dir: {Config.config_dir()}")