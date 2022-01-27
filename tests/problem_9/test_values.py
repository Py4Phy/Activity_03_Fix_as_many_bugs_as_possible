import pytest

from ..tst import _test_variable

FILENAME = "bug_09.py"

@pytest.mark.timeout(1)
def test_times():
    reference = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    return _test_variable('times',
                          reference,
                          FILENAME)

@pytest.mark.timeout(1)
def test_positions():
    reference = [0.0, -4.905, -19.62, -44.145,
                 -78.48, -122.625, -176.580,
                 -240.345, -313.92, -397.305, -490.5]
    return _test_variable('positions',
                          reference,
                          FILENAME)
