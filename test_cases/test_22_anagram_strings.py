
import importlib

module = importlib.import_module("22_anagram_strings")
is_anagram = module.is_anagram


def test_basic_anagram():
    assert is_anagram("listen", "silent") is True


def test_not_anagram():
    assert is_anagram("hello", "world") is False


def test_uppercase_letters():
    assert is_anagram("LISTEN", "silent") is True


def test_spaces():
    assert is_anagram("rail safety", "fairy tales") is True


def test_different_lengths():
    assert is_anagram("cat", "cats") is False
