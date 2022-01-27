# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 03 (Fix as many bugs as possible!)
# PROBLEM NUMBER: 4

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output, assert_python3

FILENAME = 'bug_04.py'
POINTS = 3

def test_python3():
    assert_python3()

def test_imports_math():
    return _test_output(FILENAME,
                        r"""-0\.001083[0-9]*""",
                        input_values=None,
                        regex=True)


