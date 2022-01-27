import pytest

from ..tst import _test_output

FILENAME = "bug_09.py"

@pytest.mark.timeout(1)
def test_print_values():
    return _test_output(FILENAME, r"\[[0-9., ]+\]\s*\[[-0-9., ]+\]")
