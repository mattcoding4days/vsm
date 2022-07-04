"""
Main file
"""

# standard lib
import sys
from pathlib import Path

# package
from vim_session_manager import Config, EXIT_FAILURE, EXIT_SUCCESS
from vim_session_manager.manager import VimSessionManager
from vim_session_manager.utils import Shell, VimVariant, FileSystem
from vim_session_manager.cli import Cli, SubCommand
from vim_session_manager.log import Log

# 3rd party
from result import Ok, Err


def list_sessions(vsm: VimSessionManager) -> int:
    """
    @param vsm, an instance of a VimSessionManager object
    @returns exit status
    """
    vsm.list_sessions()
    return EXIT_SUCCESS


def remove_session(vsm: VimSessionManager, session: Path | None) -> int:
    """
    @param vsm, an instance of a VimSessionManager object
    @param session, absolute path to the session file
    @returns exit status
    """
    match vsm.remove_session(session):
        case Ok(value):
            if type(value) is list:
                for s in value:
                    Log.warn(f"Removing session -> {s}")
                    s.unlink()
            else:
                Log.warn(f"Removing session -> {value}")
                value.unlink()  # TODO ignore this linting error

            Log.info("Done..")
        case Err(e):
            Log.error(e)
            return EXIT_FAILURE

    return EXIT_SUCCESS


def open_session(vsm: VimSessionManager, session: Path | None, shell: Shell, vim_executable: str) -> int:
    """
    @param vsm, an instance of a VimSessionManager object
    @param session, absolute path to the session file
    @param shell, Shell wrapper instance
    @param vim_executable, absolute path to the vim variant executable
    @returns exit status
    """
    match vsm.open_session(session):
        case Ok(value):
            Log.info(f"opening session -> {value}")
            match shell.execute(f"{vim_executable} -S {value}"):
                case Err(fail):
                    Log.error(fail)
                    return EXIT_FAILURE
        case Err(e):
            Log.error(e)
            return EXIT_FAILURE

    return EXIT_SUCCESS


def main() -> int:
    """
    @description: main program logic

    @returns: exit status
    """
    # preflight checks
    # TODO: Nix should be checked as os, distro information could be stored,
    exit_code = int()
    try:
        shell = Shell()
        fs = FileSystem(Config.config_dir(), Config.cache_dir(),
                        Config.vim_variant_file(), Config.vsm_env_var(), Config.default_sessions_directory())
        vim = VimVariant(shell, fs)
        if not vim.vim_executable:
            Log.error("No variant of vim was found on your system")
            return EXIT_FAILURE

        cli = Cli()
        session: Path | None = None
        match cli.active_command:
            case SubCommand.LIST:
                exit_code = list_sessions(
                    VimSessionManager(fs.sessions_directory()))

            case SubCommand.REMOVE:
                if cli.args.name:
                    session = Path(cli.args.name)

                exit_code = remove_session(
                    VimSessionManager(fs.sessions_directory()), session)

            case SubCommand.OPEN:
                if cli.args.name:
                    session = Path(cli.args.name)

                exit_code = open_session(
                    VimSessionManager(fs.sessions_directory()), session, shell, vim.vim_executable)

            case _:
                Log.error(
                    f"No arguments given, please use `{Config.executable()} --help` for usage information")
                exit_code = EXIT_FAILURE

    except KeyboardInterrupt:
        Log.warn("Request cancelled")
        exit_code = EXIT_FAILURE

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
