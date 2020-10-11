# !/usr/bin/python
# coding=UTF-8
# Written by Suma Kori <suma.kori93@gmail.com>, October 2020

"""This script is used to perform test cases on FibonacciSeries.

- author: Suma Kori
- e-mail: suma.kori93@gmail.com
"""

import pytest
from fibonacci import fibonacci_series

def test_find_fibonacci_series_equals():
    """This method is used to test fibonacci series if equal"""

    test_instance_fib = fibonacci_series.FibonacciSeries(2)
    assert test_instance_fib.find_fibonacci_series(2) == 5

def test_find_fibonacci_series_not_equals():
    """This method is used to test fibonacci series if not equal"""
    test_instance_fib = fibonacci_series.FibonacciSeries(2)
    assert test_instance_fib.find_fibonacci_series(2) != 4

def test_prepare_series_in_range():
    """This method is used to test fibonacci series if in range"""
    test_instance_fib = fibonacci_series.FibonacciSeries(2)
    list_below_range = []
    actual_series = []
    for idx in range(11):
        actual_series.append(test_instance_fib.find_fibonacci_series(idx))

    for idx, value in enumerate(actual_series):
        if actual_series[idx] < 11:
            list_below_range.append(value)

    assert list_below_range == [2, 3, 5, 8]
