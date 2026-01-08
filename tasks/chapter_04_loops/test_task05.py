from tasks.chapter_04_loops import task05

def test_countdown():
    expected = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert task05.countdown(10) == expected, "countdown(10) should return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]"

def test_countdown_small():
    expected = [3, 2, 1]
    assert task05.countdown(3) == expected, "countdown(3) should return [3, 2, 1]"