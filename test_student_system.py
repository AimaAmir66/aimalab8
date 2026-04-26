from student_system import login, calculate_average


def test_login_success():
    assert login("admin", "1234") == True


def test_login_fail():
    assert login("user", "wrong") == False


def test_average():
    assert calculate_average([80, 90]) == 85