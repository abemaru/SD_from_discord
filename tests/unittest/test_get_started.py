'''testing for get_started.py'''
import pytest

from starter.get_started import (
    file_exists,
    valid_keyinput,
    valid_token,
    set_url
)


class TestFileExists:
    def test_return_true_when_env_file_exists(self, mocker):
        mocker.patch('os.listdir', return_value=['.env'])
        assert file_exists() == True

    def test_return_false_when_env_file_does_not_exist(self, mocker):
        mocker.patch('os.listdir', return_value=[])
        assert file_exists() == False


class TestValidKeyinput:
    def test_return_true_when_input_is_Y(self):
        assert valid_keyinput('Y') == True

    def test_return_true_when_input_is_n(self):
        assert valid_keyinput('n') == True

    def test_return_true_when_input_is_empty(self):
        assert valid_keyinput('') == True

    def test_return_false_when_input_is_not_Y_n_or_empty(self):
        assert valid_keyinput('x') == False


class TestValidToken:
    def test_return_true_when_token_is_59_characters_long(self):
        assert valid_token('a'*59) == True

    def test_return_false_when_token_is_not_59_characters_long(self):
        assert valid_token('a'*58) == False


class TestSetUrl:
    def test_return_localhost_7860_when_url_is_empty(self):
        assert set_url('') == 'http://127.0.0.1:7860'

    def test_return_url_when_url_is_not_empty(self):
        assert set_url('http://localhost:7860') == 'http://localhost:7860'
