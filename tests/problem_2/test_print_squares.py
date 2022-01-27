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

def test_print_squares():
    return _test_output(FILENAME,
                        r"""0\s+1\s*4\s*9\s*16\s*25\s*36\s*49\s*64\s*81\s*Done""",
                        input_values=None,
                        regex=True)


