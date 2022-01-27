# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 03 (Fix as many bugs as possible!)
# PROBLEM NUMBER: 1

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output, assert_python3

FILENAME = 'bug_01.py'
POINTS = 1

def test_python3():
    assert_python3()

def test_print_sequence():
    return _test_output(FILENAME,
                        r"""0\s+1\s*2\s*3\s*4\s*5\s*6\s*7\s*8\s*9""",
                        input_values=None,
                        regex=True)


