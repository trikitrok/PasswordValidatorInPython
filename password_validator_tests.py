from password_validator import PasswordValidator


def test_a_strong_password():
    validator = PasswordValidator(8)
    assert validator.is_strong_password("#Ab3cccc")
