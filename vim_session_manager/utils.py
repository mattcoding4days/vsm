"""
Generic Utility classes
"""

# standard lib
import os
import subprocess as sp
from pathlib import Path

# package
from vim_session_manager import Config
from vim_session_manager.log import Log

# 3rd party
from result import Ok, Err, Result


class EnvironmentManager:
    """
    @description: A wrapper around any environment specific code
    """

    @staticmethod
    def get_sessions_directory() -> Path:
        """
        @description: determines if the user has defined VIM_SESSIONS environment
        variable on their system, and takes the appropriate action, returning the Path
        representation of it
        """
        session_dir = Path()
        try:
            if os.environ[Config.vsm_env_var()]:
                # if Environment variable exists, the user has the acumen
                session_dir = Path(os.environ[Config.vsm_env_var()])
        except KeyError:
            # the user does NOT have the acumen, as they havn't bothered defining the VIM_SESSIONS env var,
            # so we fallback to the default
            session_dir = Config.default_sessions_directory()
            Log.warn(
                f"{Config.vsm_env_var()} was not found on the system, defaulting to {session_dir} as a session file storage location")

        if not session_dir.is_dir():
            # TODO: A prompt library should be implemented here to verify if they user wants
            # to use the default location
            # Feature flag
            Log.warn(f"{session_dir} does not exist, so I am creating it..")
            session_dir.mkdir(parents=True)

        return session_dir


class ShellManager:
    """
    @description: A wrapper around subprocess
    """

    def __init__(self):
        self.__user_shell = str(os.getenv("SHELL"))

    def execute(self, command: str) -> Result[bool, str]:
        """
        @description: Execute a shell command

        @returns: Result[Ok, Err]
        """
        try:
            sp.run(command, check=False, shell=True,
                   executable=self.__user_shell)
        except sp.CalledProcessError as error:
            return Err(str(error))

        return Ok(True)

    def is_installed(self, command: str) -> bool:
        """
        @description: Check if a program is installed on the system, will only work for software
        that is in the users PATH, uses the POSIX compliant command -v, rather than which

        @returns: True, False
        """
        cmd = f"command -v {command}"
        ret: sp.CompletedProcess = sp.run(
            cmd, check=False, capture_output=True, shell=True, executable=self.__user_shell
        )
        if ret.returncode != 0:
            # the program is not installed
            return False

        return True
