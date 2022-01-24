"""
Session Manager Logic is stored here
"""
# standard lib
from pathlib import Path
from typing import List
import re

# package
from vsm import ThreadSafeMeta
from vsm.utils import EnvironmentManager
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

    def __validate_one(self, valid_matches: List[Path], session: Path) -> Result[Path, str]:
        """
        @description: validates that exactly one match was found

        @param: The session file to check for

        @return: Result containing the Path of said Ok(Path), if it was
        not found, Err(str)
        """
        # if the list is empty we found no sessions
        if not valid_matches:
            return Err(f"No matches were found for session named: {session}")

        # regex matched more than one session, so we don't know which one to load.
        # TODO: add a feature which allows the user to select from the ambiguos sessions
        # Feature Flag
        if len(valid_matches) > 1:
            for match in valid_matches:
                Log.warn(f"Found: {match}")
            return Err(f"Ambiguous session name: {session}")

        return Ok(valid_matches[0])

    def __fetch(self, session: Path) -> Result[Path, str]:
        """
        @description: wrap up common functionality

        @param: session, the name of the session file the user wants
        """
        matches: List[Path] = self.__match_session(session)
        return self.__validate_one(matches, session)

    def list_sessions(self) -> None:
        """
        @description: called when used passes the -l command line parameter,
        prints out all session files
        """
        # TODO: Just printing out the session files on new lines is pretty lame,
        # the rich python library could be used to display the files and information
        # about the files in a tabular format.
        # Feature Flag
        if not self.__all_sessions:
            Log.warn("No session files found, you better get to work")
        else:
            for session in self.__all_sessions:
                Log.info(session.stem)

    def remove_session(self, session: Path) -> Result[Path, str]:
        """
        @description: called when used passes the -r command line parameter,
        removes the session file if it exists

        @param: session, the name of the session file the user wants to delete

        @return Result[Ok(Path), Err(str)]
        """
        return self.__fetch(session)

    def open_session(self, session: Path) -> Result[Path, str]:
        """
        @description: called when used passes the -o command line parameter,
        opens the specified session file, if it exists

        @param: session, the name of the session file the user wants to load

        @return Result[Ok(Path), Err(str)]
        """
        return self.__fetch(session)

    def the_current_state_of_things(self) -> None:
        """
        @description: called when used passes the --the_current_state_of_things
        """
        # TODO: This could be quite a robust feature, show information about vsm,
        # version, user name, distro type/name. Show statistical information about vim session files,
        # like how long the user had the file open (how long they were working on the project), last time
        # the file was opened etcetra. This could be shown in a pretty tabluar colored format using the rich python library.
        # Feature flag
        ...
