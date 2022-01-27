# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 03 (Fix as many bugs as possible!)
# PROBLEM NUMBER: 2

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output, assert_python3

FILENAME = 'bug_02.py'
POINTS = 2

def test_python3():
    assert_python3()

def test_runs():
    return _test_output(FILENAME,
                        r"""Done""",
                        input_values=None,
                        regex=False)


