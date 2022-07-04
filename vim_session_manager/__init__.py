"""
Package wide configurations
"""
from pathlib import Path
from threading import Lock
from typing import Any, Dict, List

EXIT_SUCCESS: int = 0
EXIT_FAILURE: int = 1

# TODO: There are many different variations of vim, they need all
# need to be added to this list
VIM_VARIENTS: List[str] = ['nvim', 'vim', 'gvim']


class ThreadSafeMeta(type):
    """
    @description This is a thread-safe implementation of a Singleton.
    """
    _instances: Dict[Any, Any] = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        @description Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        # Now, imagine that the program has just been launched. Since there's
        # no Singleton instance yet, multiple threads can simultaneously pass
        # the previous conditional and reach this point almost at the same
        # time. The first of them will acquire lock and will proceed further,
        # while the rest will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves
            # the lock block, a thread that might have been waiting for the
            # lock release may then enter this section. But since the Singleton
            # field is already initialized, the thread won't create a new
            # object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Config(metaclass=ThreadSafeMeta):
    """
    @description: Global program configuration, uses the dotenv package
    to load runtime configuration from a .env file, once and
    only once into this object, this object can be used through-out
    the code base
    """
    __package: str = __package__
    __version: str = "0.1.3"
    __executable: str = "vsm"
    __base_dir: Path = Path(__file__).resolve(strict=True).parent.parent.parent
    __config_dir: Path = Path.home() / ".config" / __package
    __cache_dir: Path = Path.home() / ".cache" / __package
    __vim_variant_file: Path = __config_dir / 'vim_variant.json'
    __vsm_env_var: str = "VIM_SESSIONS"
    __default_sessions_directory: Path = Path.home() / ".config" / "vim_sessions"

    @classmethod
    def package(cls) -> str:
        """
        @description: getter for package name
        """
        return cls.__package

    @classmethod
    def version(cls) -> str:
        """
        @description: getter for version of package
        """
        return cls.__version

    @classmethod
    def executable(cls) -> str:
        """
        @description: getter for executable name
        """
        return cls.__executable

    @classmethod
    def base_dir(cls) -> Path:
        """
        @description: getter for base directory
        """
        return cls.__base_dir

    @classmethod
    def config_dir(cls) -> Path:
        """
        @description: getter for the configuration directory
        """
        return cls.__config_dir

    @classmethod
    def cache_dir(cls) -> Path:
        """
        @description: getter for the cacheing directory
        """
        return cls.__cache_dir

    @classmethod
    def vim_variant_file(cls) -> Path:
        """
        @description: getter for the vim variant file location
        """
        return cls.__vim_variant_file

    @classmethod
    def vsm_env_var(cls) -> str:
        """
        @description: Get the environment variable name
        """
        return cls.__vsm_env_var

    @classmethod
    def default_sessions_directory(cls) -> Path:
        """
        @description: Get the default sessions directory
        """
        return cls.__default_sessions_directory
