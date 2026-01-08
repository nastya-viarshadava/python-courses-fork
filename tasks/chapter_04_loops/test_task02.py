from tasks.chapter_04_loops import task02

def test_sum_until_zero_or_less_with_zero():
    assert task02.sum_until_zero_or_less([1, 2, 3, 0, 4]) == 6, "sum_until_zero_or_less([1, 2, 3, 0, 4]) should return 6"

def test_sum_until_zero_or_less_no_zero():
    assert task02.sum_until_zero_or_less([1, 2, 3, 4]) == 10, "sum_until_zero_or_less([1, 2, 3, 4]) should return 10"

def test_sum_until_zero_or_less_zero_first():
    assert task02.sum_until_zero_or_less([0, 1, 2]) == 0, "sum_until_zero_or_less([0, 1, 2]) should return 0"

def test_sum_until_zero_or_less_empty():
    assert task02.sum_until_zero_or_less([]) == 0, "sum_until_zero_or_less([]) should return 0"

def test_sum_until_zero_or_less_with_negative():
    assert task02.sum_until_zero_or_less([1, 2, -1, 3]) == 3, "sum_until_zero_or_less([1, 2, -1, 3]) should return 3"