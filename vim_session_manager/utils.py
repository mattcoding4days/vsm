"""
Generic Utility classes
"""

# standard lib
import os
import subprocess as sp
from pathlib import Path
from typing import List
import json

# package
from vim_session_manager import Config, VIM_VARIENTS, ThreadSafeMeta
from vim_session_manager.log import Log
from vim_session_manager.prompt import PromptSingleSelection

# 3rd party
from result import Ok, Err, Result


class FileSystem(metaclass=ThreadSafeMeta):
    """
    @description Wrap up caching and configuration
    file creation, reading, writing functionality, relies
    on dependency injection to reduce object coupling

    @param config_dir Config.config_dir()
    @param cache_dir Config.cache_dir()
    @param vim_variant Config.vim_variant()
    @param vsm_env_var Config.vsm_env_var()
    @param default_sessions_directory Config.default_sessions_directory()
    """

    def __init__(self, config_dir: Path, cache_dir: Path, vim_variant: Path, vsm_env_var: str, default_sessions_directory: Path):
        self.__config_dir = config_dir
        self.__cache_dir = cache_dir
        self.__vim_variant_file = vim_variant
        self.__vsm_env_var = vsm_env_var
        self.__default_sessions_directory = default_sessions_directory

        if not self.__config_dir.exists():
            self.__config_dir.mkdir(parents=True)

        if not self.__cache_dir.exists():
            self.__cache_dir.mkdir(parents=True)

    @property
    def config_dir(self) -> Path:
        """
        @description getter
        """
        return self.__vim_variant_file

    @property
    def cache_dir(self) -> Path:
        """
        @description getter
        """
        return self.__vim_variant_file

    @property
    def vim_variant_file(self) -> Path:
        """
        @description getter
        """
        return self.__vim_variant_file

    def sessions_directory(self) -> Path:
        """
        @description: determines if the user has defined VIM_SESSIONS environment
        variable on their system, and takes the appropriate action, returning the Path
        representation of it
        """
        session_dir = Path()
        try:
            if os.environ[self.__vsm_env_var]:
                # if Environment variable exists, the user has the acumen
                session_dir = Path(os.environ[self.__vsm_env_var])
        except KeyError:
            # the user does NOT have the acumen, as they havn't bothered defining the VIM_SESSIONS env var,
            # so we fallback to the default
            session_dir = self.__default_sessions_directory
            Log.warn(
                f"{self.__vsm_env_var} was not found on the system, defaulting to {session_dir} as a session file storage location")

        if not session_dir.is_dir():
            # TODO: A prompt library should be implemented here to verify if they user wants
            # to use the default location
            # Feature flag
            Log.warn(f"{session_dir} does not exist, so I am creating it..")
            session_dir.mkdir(parents=True)

        return session_dir

    def read_vim_variant(self) -> Result[str, str]:
        """
        @description attempt to read the file and return
        the 'variant' value if the file exists and is not empty

        @return Result with Ok/Err
        """
        if not self.__vim_variant_file.exists():
            return Err(f"{self.__vim_variant_file} does not exist")

        with open(self.vim_variant_file, 'r') as f:
            data = json.load(f)

        if not data:
            return Err(f"{self.__vim_variant_file} was empty")

        return Ok(data['variant'])

    def write_vim_variant(self, variant: str):
        """
        @description Write the users chosen vim variant
        to disk in json format. Note that this will overrite
        the file if it already exists
        """
        data = {"variant": "{0}".format(variant)}
        with open(self.__vim_variant_file, 'w') as f:
            json.dump(data, f)


class Shell:
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


class VimVariant:
    """
    @description Helper class to discover if any variant of
    vim is installed on the system, Note that the vim install
    must be in the users $PATH variable. If there are multiple vim
    variants found on the system, the user will be presented with a prompt
    to make a choice for which variant they wish to use. vsm will then save that
    selection to disk for future use
    """

    def __init__(self, shell: Shell, fs: FileSystem):
        """
        @param shell vim_session_manager.utils.Shell instance
        @param fs vim_session_manager.utils.FileSystem instance

        @raise KeyboardInterrupt
        """
        # NOTE: if the user has multiple vim variants installed on the
        # system, the first on in the list will be used. This really isn't
        # ideal.
        # TODO: There needs to be a way for the user to select the variant they want
        # on first run, then cache that selection to a file for future use
        self.__vim_executable: str | None = None
        self.__vim_executables: List[str] = []

        match fs.read_vim_variant():
            case Ok(value):
                self.__vim_executable = value
            case Err(e):
                Log.warn(e)
                for variant in VIM_VARIENTS:
                    if shell.is_installed(variant):
                        self.__vim_executables.append(variant)

                if len(self.__vim_executables) == 1:
                    self.__vim_executable = self.__vim_executables[0]
                    self.__save_variant_choice(fs)

                if len(self.__vim_executables) > 1:
                    prompt = PromptSingleSelection(
                        "Multiple vim variants found on the system, please make a selection", self.__vim_executables)
                    prompt.show_prompt()
                    self.__vim_executable = prompt.selection()
                    if self.__vim_executable:
                        self.__save_variant_choice(fs)
                    else:
                        Log.error("Selection was empty")

    def __save_variant_choice(self, fs: FileSystem):
        """
        @description log and create/write the file
        """
        # TODO: this if is only here to stop pyright warnings, need
        # to add the proper pyright ignore code
        if self.__vim_executable:
            Log.info(f"saving selection to {fs.vim_variant_file}")
            fs.write_vim_variant(self.__vim_executable)

    @property
    def vim_executable(self) -> str | None:
        """
        @description if this value is None no valid install of
        any known variation of vim was found on the system
        """
        return self.__vim_executable
