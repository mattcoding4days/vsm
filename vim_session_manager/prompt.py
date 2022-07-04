"""
Wrapper around the inquirer package
"""
# standard library
import abc
from typing import List, Any

# 3rd party
import inquirer


class IPrompt(metaclass=abc.ABCMeta):
    """
    @description Interface for different interactive prompts
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'show_prompt') and
                callable(subclass.show_prompt) and
                hasattr(subclass, 'selection') and
                callable(subclass.selection) or
                NotImplemented)

    @abc.abstractmethod
    def show_prompt(self):
        """
        @description show the interactive prompt to the user
        """
        raise NotImplementedError

    @abc.abstractmethod
    def selection(self) -> str | List[str]:
        """
        @description retrieve the selction from the prompt dictionary
        """
        raise NotImplementedError


class PromptSingleSelection(IPrompt):
    def __init__(self, message: str, choices: List[str]):
        self.inquirer_list: List[inquirer.List] = [inquirer.List(
            'index', message=message, choices=choices, carousel=True)]
        self.__selection: dict[Any, Any] | None = None

    def show_prompt(self):
        """
        @description Overrides __Prompt.show_prompt()
        @raise KeyboardInterrupt if user ctrl+c
        """
        self.__selection = inquirer.prompt(
            self.inquirer_list, raise_keyboard_interrupt=True)

    def selection(self) -> str | None:
        """
        @description Overrides __Prompt.selection()
        @return Will only return a single selection as a string, or None
        """
        if self.__selection:
            return str(self.__selection['index'])
        return None


class PromptMultiSelection(IPrompt):
    def __init__(self, message: str, choices: List[str]):
        self.inquirer_list: List[inquirer.Checkbox] = [inquirer.Checkbox(
            'index', message=message, choices=choices, carousel=True)]
        self.__selection: dict[Any, Any] | None = None

    def show_prompt(self):
        """
        @description Overrides __Prompt.show_prompt()
        @raise KeyboardInterrupt if user ctrl+c
        """
        self.__selection = inquirer.prompt(
            self.inquirer_list, raise_keyboard_interrupt=True)

    def selection(self) -> List[str] | None:
        """
        @description Overrides __Prompt.selection()
        @return Will only return a single selection as a string, or None
        """
        if self.__selection:
            return self.__selection['index']
        return None
