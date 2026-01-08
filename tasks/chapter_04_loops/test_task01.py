from tasks.chapter_04_loops import task01

def test_count_up():
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert task01.count_up(10) == expected, "count_up(10) should return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"

def test_count_up_small():
    expected = [1, 2, 3, 4, 5]
    assert task01.count_up(5) == expected, "count_up(5) should return [1, 2, 3, 4, 5]"