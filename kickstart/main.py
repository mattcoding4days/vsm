"""
Example Driver code
"""
# standard lib

# package
from kickstart import Config
from kickstart.logger import pkg_logger as pl
from kickstart.command_line import Cli

# create the logger at module level
Log = pl.Logger().get_logger()


def run() -> None:
    """
    Example function to execute through poetry scripts
    """
    cli = Cli()
    if cli.args.run:
        Log.debug('Received -r as a command line argument')

    try:
        Log.info("APP_ENV: %s :: package name: %s@%s",
                    Config.env(), Config.package(), Config.version())
    except KeyError as error:
        Log.error(
            'Could not find %s in .env file. Please consult the README', error)
        Log.info('Testing for %s@%s', Config.package(), Config.version())
        Log.debug('Testing for %s@%s', Config.package(), Config.version())
        Log.warning('Testing for %s@%s', Config.package(), Config.version())
        Log.error('Testing for %s@%s', Config.package(), Config.version())
