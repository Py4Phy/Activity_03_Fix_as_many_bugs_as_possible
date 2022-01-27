# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 03 (Fix as many bugs as possible!)
# PROBLEM NUMBER: 7

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_function

FILENAME = 'bug_07.py'
POINTS = 5

@pytest.mark.parametrize(("args", "kwargs", "reference"),
                         list(zip([[-6.28318531], [-5.23598776], [-4.1887902], [-3.14159265], [-2.0943951], [-1.04719755], [0.0], [1.04719755], [2.0943951], [3.14159265], [4.1887902], [5.23598776], [6.28318531]], [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}], [4.488828102926136e-10, -0.16539866811604859, -0.20674833544808308, 1.1426666120579356e-09, 0.4134966726101663, 0.8269933435063325, 1.0, 0.8269933435063325, 0.4134966726101663, 1.1426666120579356e-09, -0.20674833544808308, -0.16539866811604859, 4.488828102926136e-10])))
def test_sinc(args, kwargs, reference):
    return _test_function("sinc",
                          args,     # tuple or list
                          kwargs,   # dict
                          reference,
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )

