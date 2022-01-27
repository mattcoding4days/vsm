"""
Showcasing two different ways to properly test your code

1. By importing the package in directly.
2. By passing in a function fixture defined in conftest.py
"""
from vim_session_manager import Config


def test_version_using_fixture(pkg_test):
    """
    testing version from passing the module
    in as a fixture
    """
    assert pkg_test.Config.package() == 'vim_session_manager'


def test_package_name():
    """
    testing version from importing it
    """
    assert Config.package() == 'vim_session_manager'
