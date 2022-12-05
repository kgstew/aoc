import pytest
from puzzle_4 import check_contained


def test_check_contained():
    # zones = ["2-4,6-8",
    #         "2-3,4-5",
    #         "5-7,7-9",
    #         "2-8,3-7",
    #         "6-6,4-6",
    #         "2-6,4-8"]
    print("here")
    assert (check_contained([3, 7], [2, 8]) == True)
    assert (check_contained([2, 4], [2, 4]) == True)
    assert (check_contained([2, 2], [2, 4]) == True)
    assert (check_contained([3, 4], [2, 4]) == True)
    assert (check_contained([4, 4], [2, 4]) == True)
    assert (check_contained([1, 4], [2, 4]) == True)
