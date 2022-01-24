"""
Generic Utility classes
"""

# standard lib
import os
import subprocess as sp
from pathlib import Path

# package
from vsm import Config
from vsm.log import Log


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
                # if Environment variable exists, return this as the users desired storage
                # location for their session files
                session_dir = Path(os.environ[Config.vsm_env_var()])
        except KeyError:
            # the user has not bothered defining the VIM_SESSION env variable so use the default storage location
            session_dir = Config.default_sessions_directory()
            Log.warn(
                f"{Config.vsm_env_var()} was not found on the system, defaulting to {session_dir} as a session file storage location")

        if not session_dir.is_dir():
            # TODO: A prompt library should be implemented here to verify if they user wants
            # to use the default location
            Log.warn(f"{session_dir} does not exist, so I am creating it..")
            session_dir.mkdir(parents=True)

        return session_dir


class ShellManager:
    """
    @description: A wrapper around subprocess
    """

    def __init__(self):
        self.__user_shell = str(os.getenv("SHELL"))

    def execute(self, command: str):
        """
        @description: Execute a shell command

        @returns: Result[Ok, Err]
        """
        try:
            sp.run(command, check=False, shell=True,
                   executable=self.__user_shell)
        except sp.CalledProcessError as error:
            Log.error(str(error))

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
