# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 03 (Fix as many bugs as possible!)
# PROBLEM NUMBER: 7

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_function

FILENAME = 'bug_07.py'
POINTS = 1

@pytest.mark.parametrize(("args", "kwargs", "reference"),
                         list(zip([[0.001], [1e-06], [1e-16]], [{}, {}, {}], [0.9999998333333416, 0.9999999999998334, 1.0])))
def test_small(args, kwargs, reference):
    return _test_function("sinc",
                          args,     # tuple or list
                          kwargs,   # dict
                          reference,
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )

