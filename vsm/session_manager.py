"""
Session Manager Logic is stored here
"""
# standard lib
from pathlib import Path
from typing import List
import re

# package
from vsm import ThreadSafeMeta
from vsm.utils import EnvironmentManager, ShellManager
from vsm.log import Log

# 3rd party
from result import Ok, Err, Result


class VimSessionManager(metaclass=ThreadSafeMeta):
    """
    Implements all functionality of other classes, to orchestrate the program
    """

    def __init__(self):
        self.__sessions_dir: Path = EnvironmentManager().get_sessions_directory()
        self.__all_sessions: List[Path] = self.__load_sessions()
        self.shell = ShellManager()

    def __load_sessions(self) -> List[Path]:
        """
        @description: load all the sessions on disc
        @returns a list of Path objects
        """
        sessions: List[Path] = []
        for session in self.__sessions_dir.iterdir():
            # filter the files by file extension
            if session.suffix == ".vim":
                sessions.append(session)

        return sessions

    def __match_session(self, source: Path) -> List[Path]:
        """
        @description: check to see if we have a file match, used
        when a user wants to load a session or remove a session

        @param: source argument given to script by user
        @return: list of matched sessions
        """
        matches: List[Path] = []
        for session in self.__all_sessions:
            pattern = re.compile(source.stem)
            if pattern.match(session.stem):
                matches.append(session)

        return matches

    def open_session(self, session: Path) -> Result[bool, str]:
        """
        @description: called when used passes the -o command line parameter,
        opens the specified session file, if it exists

        @param: session, the session file the user wants to load
        """
        ...

    def list_sessions(self) -> None:
        """
        @description: called when used passes the -l command line parameter,
        prints out all session files
        """
        for session in self.__all_sessions:
            Log.info(str(session.stem))

    def remove_session(self) -> Result[bool, str]:
        """
        @description: called when used passes the -r command line parameter,
        removes the session file if it exists
        """
        ...

    def info(self) -> None:
        """
        @description: called when used passes the -i command line parameter,
        shows all information about vsm
        """
        ...
