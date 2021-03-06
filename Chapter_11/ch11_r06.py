"""Python Cookbook 2nd ed.

Chapter 11, recipe 6 and 7. Pytest and Doctest.
"""

from Chapter_11.ch11_r01 import Summary

from pytest import *  # type: ignore
import random


@fixture  # type: ignore
def flat_data():
    data = list(range(1001))
    random.shuffle(data)
    return data


def test_flat(flat_data):
    summary = Summary()
    for sample in flat_data:
        summary.add(sample)
    assert summary.mean == 500
    assert summary.median == 500


@fixture  # type: ignore
def biased_data():
    # Build 500 elements: each with the same large value of 97.
    data = [500] * 97
    # Build 903 elements: each value of n occurs n times.
    for i in range(1, 43):
        data += [i] * i
    random.shuffle(data)
    return data


def test_biased(biased_data):
    summary = Summary()
    for sample in biased_data:
        summary.add(sample)
    assert summary.mean == approx(74.085)
    assert summary.median == approx(32.0)
    top_3 = summary.mode[:3]
    assert top_3 == [(500, 97), (42, 42), (41, 41)]


# Need to use a complex command line to combine both.
# pytest Chapter_11/ch11_r06.py --doctest-modules Chapter_11/ch11_r01.py
