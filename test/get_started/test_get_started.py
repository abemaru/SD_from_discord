'''testing for get_started.py'''
import pytest

from get_started import get_started


def test_get_started():
    '''testing for get_started'''
    assert get_started() == 'Hello, World!'

