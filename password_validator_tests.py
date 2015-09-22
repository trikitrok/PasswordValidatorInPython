import pytest
from password_validator import PasswordValidator


@pytest.fixture
def validator():
    return PasswordValidator(8)


def test_a_strong_password(validator):
    assert validator.is_strong_password("#Ab3cccc")


def test_that_only_passwords_with_the_minimum_length_are_strong(validator):
    assert validator.is_strong_password("#Ab3ccc") is False


def test_that_only_passwords_including_numbers_are_strong(validator):
    assert validator.is_strong_password("#Abccccc") is False


def test_that_only_passwords_including_upper_case_letters_are_strong(validator):
    assert validator.is_strong_password("#ab3cccc") is False


def test_that_only_passwords_including_lower_case_letters_are_strong(validator):
    assert validator.is_strong_password("#AB3CCCC") is False


def test_that_only_passwords_including_special_characters_are_strong(validator):
    assert validator.is_strong_password("cAb3cccc") is False
