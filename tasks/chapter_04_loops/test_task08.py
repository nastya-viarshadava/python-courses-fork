from tasks.chapter_04_loops import task08

def test_login_attempts_success():
    assert task08.login_attempts(["password123", "qwerty", "secret"], "secret", 3) == True, "login_attempts with correct password within attempts limit should return True"

def test_login_attempts_fail():
    assert task08.login_attempts(["letmein", "admin123", "guest", "user"], "pass", 2) == False, "login_attempts with incorrect password exceeding limit should return False"

def test_login_attempts_more_than_limit():
    assert task08.login_attempts(["abc123", "123456", "monkey", "key"], "key", 2) == False, "login_attempts with correct password after limit should return False"

def test_login_attempts_immediate():
    assert task08.login_attempts(["open", "sesame", "trustno1"], "open", 4) == True, "login_attempts with correct password on first try should return True"