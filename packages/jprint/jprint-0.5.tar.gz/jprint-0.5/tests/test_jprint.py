import pytest

from jprint import jprint, format


def test_dictionary():
    out = format({"a": 1, "b": 2, "c": 3})
    assert out == '{\n    "a": 1,\n    "b": 2,\n    "c": 3\n}'


def test_json_string():
    out = format('{"a": 1, "b": 2, "c": 3}')
    assert out == '''"{\\\"a\\\": 1, \\\"b\\\": 2, \\\"c\\\": 3}"'''


def test_non_json_string():
    out = format("This is not a valid JSON string")
    assert out == '"This is not a valid JSON string"'
