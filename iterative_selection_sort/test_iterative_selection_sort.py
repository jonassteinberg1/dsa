from iterative_selection_sort import iterative_selection_sort
import pytest

def test_alternating_zeroes_and_ones():
    arr = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert iterative_selection_sort(arr) == sorted(arr)

def test_increasing_decreasing():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert iterative_selection_sort(arr) == sorted(arr)

def test_decreasing_increasing():
    arr = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] + list(range(1, 20))
    assert iterative_selection_sort(arr) == sorted(arr)

def test_all_but_one_element_the_same():
    arr = [0] * 19 + [1]
    assert iterative_selection_sort(arr) == sorted(arr)

def test_all_but_one_element_the_same_big_delta():
    arr = [1] * 19 + [100]
    assert iterative_selection_sort(arr) == sorted(arr)

def test_large_range():
    arr = [-100] + list(range(1, 20))
    assert iterative_selection_sort(arr) == sorted(arr)

def test_very_close_numbers():
    arr = [i/10 for i in range(20)]
    assert iterative_selection_sort(arr) == sorted(arr)

def test_all_negative_numbers():
    arr = list(range(0, -5, -1))
    assert iterative_selection_sort(arr) == sorted(arr)

def test_mix_of_positive_and_negative():
    arr = [-10, 10] * 10
    assert iterative_selection_sort(arr) == sorted(arr)

def test_alternating_high_and_low():
    arr = [20 - i if i % 2 == 0 else i for i in range(20)]
    assert iterative_selection_sort(arr) == sorted(arr)

def test_peak_in_the_middle():
    arr = [2] * 10 + [3] + [2] * 9
    assert iterative_selection_sort(arr) == sorted(arr)

def test_small_range_random_integers():
    arr = [5, 3, 0, 4, 0, 4, 4, 0, 4, 0, 0, 0, 0, 4, 1, 0, 1, 4, 3, 5]
    assert iterative_selection_sort(arr) == sorted(arr)

def test_floating_point_numbers():
    arr = [float(i) for i in range(20)]
    assert iterative_selection_sort(arr) == sorted(arr)

def test_large_value_at_the_beginning():
    arr = [1000] + list(range(1, 20))
    assert iterative_selection_sort(arr) == sorted(arr)
