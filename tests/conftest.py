"""
Define fixtures here.
Fixtures are 'setup' and 'tear down' code
for our actual function tests and unit module tests.
Any fixture defined in this module can in turn be shared
with any other test as long as it is a sub-directory of the
tests folder.

Never include this module in any other modules. This module is
technically a 'plugin', pytest recognizes it as such and uses it
correctly
"""
# pylint: disable=W0621, E1101, C0103, W0612

# standard lib
import sys

# third party
import pytest

# package
import kickstart as ks

# noinspection PyCallByClass


@pytest.fixture()
def pkg_test() -> None:
    """
    test version
    """
    # Setup code
    sys.stdout.write('\nRunning setup code for module\n')

    yield ks

    # tear down code
    sys.stdout.write('Running Teardown code for module\n')
