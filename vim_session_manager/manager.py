"""
Session Manager Logic is stored here
"""
# standard lib
from pathlib import Path
from typing import List
import re

# package
from vim_session_manager import ThreadSafeMeta
from vim_session_manager.log import Log
from vim_session_manager.prompt import PromptSingleSelection, PromptMultiSelection

# 3rd party
from result import Ok, Err, Result


class VimSessionManager(metaclass=ThreadSafeMeta):
    """
    @description Implements all functionality of other classes, to orchestrate the program

    @path sessions_dir absolute path to session file directory
    """

    def __init__(self, sessions_dir: Path):
        self.__sessions_dir = sessions_dir
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

    def list_sessions(self):
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

    def remove_session(self, session: Path | None) -> Result[Path, str] | Result[List[Path], str]:
        """
        @description: called when used passes the -r command line parameter,
        removes the session file if it exists

        @param: session, the name of the session file the user wants to delete

        @return Result[Ok(Path), Err(str)]
        """
        if session:
            return self.__fetch(session)

        stem_sessions: List[str] = []
        for session in self.__all_sessions:
            stem_sessions.append(session.stem)

        prompt = PromptMultiSelection(
            "Select all sessions you would like to remove", stem_sessions)
        prompt.show_prompt()
        selection = prompt.selection()
        if not selection:
            return Err("No sessions were selected for removal")

        matched_sessions: List[Path] = []
        for session in self.__all_sessions:
            for selected in selection:
                if session.stem == selected:
                    matched_sessions.append(session)

        return Ok(matched_sessions)

    def open_session(self, session: Path | None) -> Result[Path, str]:
        """
        @description: called when used passes the -o command line parameter,
        opens the specified session file, if it exists

        @param: session, the name of the session file the user wants to load

        @return Result[Ok(Path), Err(str)]
        """
        if session:
            return self.__fetch(session)

        stem_sessions: List[str] = []
        for session in self.__all_sessions:
            stem_sessions.append(session.stem)

        prompt = PromptSingleSelection(
            "Which session would you like to load?", stem_sessions)
        prompt.show_prompt()
        selection = prompt.selection()

        for session in self.__all_sessions:
            if session.stem == selection:
                return Ok(session)

        return Err("Session could not be loaded")
