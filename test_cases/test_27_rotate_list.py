
import importlib

module = importlib.import_module("27_rotate_list")
rotate_list = module.rotate_list


def test_normal_rotation():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_empty_list():
    assert rotate_list([], 3) == []


def test_single_element():
    assert rotate_list([7], 2) == [7]


def test_negative_rotation():
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]


def test_k_greater_than_list_length():
    assert rotate_list([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]
