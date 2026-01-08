from tasks.chapter_04_loops import task06

def test_even_numbers():
    expected = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert task06.even_numbers(20) == expected, "even_numbers(20) should return [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]"

def test_even_numbers_small():
    expected = [0, 2, 4, 6]
    assert task06.even_numbers(6) == expected, "even_numbers(6) should return [0, 2, 4, 6]"

def test_even_numbers_zero():
    expected = [0]
    assert task06.even_numbers(0) == expected, "even_numbers(0) should return [0]"