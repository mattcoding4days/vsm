"""
Main file
"""

# standard lib
import sys
from pathlib import Path

# package
from vim_session_manager import Config, EXIT_FAILURE, EXIT_SUCCESS
from vim_session_manager.manager import VimSessionManager
from vim_session_manager.utils import Shell, VimVariant
from vim_session_manager.cli import Cli
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


def remove_session(vsm: VimSessionManager, session: Path) -> int:
    """
    @param vsm, an instance of a VimSessionManager object
    @param session, absolute path to the session file
    @returns exit status
    """
    match vsm.remove_session(session):
        case Ok(value):
            Log.warn(f"Removing session -> {value}")
            # TODO: use a yes/no prompt to verify the user doesn't remove a file by accident
            value.unlink()
            Log.info("Done..")
        case Err(e):
            Log.error(e)
            return EXIT_FAILURE

    return EXIT_SUCCESS


def open_session(vsm: VimSessionManager, session: Path, shell: Shell, vim_executable: str) -> int:
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
    shell = Shell()
    vim = VimVariant(shell)
    if not vim.vim_executable:
        Log.error("No variant of vim was found on your system")
        return EXIT_FAILURE

    cli = Cli()

    exit_code = int()
    if cli.args.list_sessions:
        exit_code = list_sessions(VimSessionManager())

    elif cli.args.remove_session:
        exit_code = remove_session(
            VimSessionManager(), Path(cli.args.remove_session))

    elif cli.args.open_session:
        exit_code = open_session(
            VimSessionManager(), Path(cli.args.open_session), shell, vim.vim_executable)

    else:
        Log.error(
            f"No arguments given, please use `{Config.executable()} --help` for usage information")
        exit_code = EXIT_FAILURE

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
