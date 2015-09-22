from password_validator import PasswordValidator


def test_a_strong_password():
    validator = PasswordValidator(8)
    assert validator.is_strong_password("#Ab3cccc")


def test_a_password_under_the_minimum_length_is_not_strong():
    validator = PasswordValidator(8)
    assert validator.is_strong_password("#Ab3ccc") == False