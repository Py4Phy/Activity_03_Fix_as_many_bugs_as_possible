# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 03 (Fix as many bugs as possible!)
# PROBLEM NUMBER: 8

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'bug_08.py'
POINTS = 4

def test_sum_of_squares():
    return _test_variable("sum_s", 385,
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )
