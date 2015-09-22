from password_validator import PasswordValidator


def test_a_strong_password():
    validator = PasswordValidator(8)
    assert validator.is_strong_password("#Ab3cccc")


def test_that_only_passwords_with_the_minimum_length_are_strong():
    validator = PasswordValidator(8)
    assert validator.is_strong_password("#Ab3ccc") == False


def test_that_only_passwords_including_numbers_are_strong():
    validator = PasswordValidator(8)
    assert validator.is_strong_password("#Abccccc") == False


def test_that_only_passwords_including_upper_case_letters_are_strong():
    validator = PasswordValidator(8)
    assert validator.is_strong_password("#ab3cccc") == False


def test_that_only_passwords_including_lower_case_letters_are_strong():
    validator = PasswordValidator(8)
    assert validator.is_strong_password("#AB3CCCC") == False