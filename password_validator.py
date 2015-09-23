import re


class PasswordValidator(object):
    def __init__(self, minimum_length):
        self.minimum_length = minimum_length

    def is_strong_password(self, password):
        includes_special_characters = self._includes_any(self.REQUIRED_SPECIAL_CHARACTERS, password)
        includes_lower_case_letters = self._includes_any(self.LOWER_CASE_LETTERS, password)
        includes_upper_case_letters = self._includes_any(self.UPPER_CASE_LETTERS, password)
        includes_numbers = self._includes_any(self.NUMBERS, password)
        has_minimum_length = len(password) >= self.minimum_length
        return \
            has_minimum_length and \
            includes_numbers and \
            includes_upper_case_letters and \
            includes_lower_case_letters and \
            includes_special_characters

    @staticmethod
    def _includes_any(pattern, password):
        return re.search(pattern, password) is not None

    REQUIRED_SPECIAL_CHARACTERS = '[%#]'
    UPPER_CASE_LETTERS = '[A-Z]'
    LOWER_CASE_LETTERS = '[a-z]'
    NUMBERS = '[0-9]'
