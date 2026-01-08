from tasks.chapter_04_loops import task07

def test_words_longer_than_three():
    assert task07.words_longer_than_three(["a", "ab", "abc", "abcd", "abcde"]) == ["abcd", "abcde"], "words_longer_than_three with mixed lengths should return ['abcd', 'abcde']"

def test_words_longer_than_three_all_short():
    assert task07.words_longer_than_three(["a", "b", "c"]) == [], "words_longer_than_three with all short words should return []"

def test_words_longer_than_three_empty():
    assert task07.words_longer_than_three([]) == [], "words_longer_than_three with empty list should return []"