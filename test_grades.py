
from grades import compute_hw_average


def test_zero_grades():
    grades = []
    assert compute_hw_average(grades,0) == 0


def test_single_grade():
    grades = [42]
    assert compute_hw_average(grades,0) == 42

def test_two_grade():
        grades = [0,50]
        assert compute_hw_average(grades,0) == 25


def test_drop_grade():
    grades = [0, 50, 100]
    assert compute_hw_average(grades, 2) == 100
