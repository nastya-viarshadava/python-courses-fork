from tasks.chapter_04_loops import task03

def test_check_password_correct():
    assert task03.check_password(["wrong", "secret", "another"], "secret") == True, "check_password with correct password in list should return True"

def test_check_password_incorrect():
    assert task03.check_password(["wrong1", "wrong2"], "admin") == False, "check_password with incorrect password should return False"

def test_check_password_empty():
    assert task03.check_password([], "password") == False, "check_password with empty list should return False"

def test_check_password_first_correct():
    assert task03.check_password(["letmein", "wrong"], "letmein") == True, "check_password with correct password first should return True"