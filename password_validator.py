import re


class PasswordValidator(object):
    def __init__(self, minimum_length):
        self.minimum_length = minimum_length

    def is_strong_password(self, password):
        includes_special_characters = self._includes_special_characters(password)
        includes_lower_case_letters = self._includes_lower_case_letters(password)
        includes_upper_case_letters = self._includes_upper_case_letters(password)
        includes_numbers = self._includes_numbers(password)
        has_minimum_length = self._has_minimum_length(password)
        return \
            has_minimum_length and \
            includes_numbers and \
            includes_upper_case_letters and \
            includes_lower_case_letters and \
            includes_special_characters

    def _has_minimum_length(self, password):
        return len(password) >= self.minimum_length

    def _includes_numbers(self, password):
        return self._includes_any(self.NUMBERS, password)

    def _includes_upper_case_letters(self, password):
        return self._includes_any(self.UPPER_CASE_LETTERS, password)

    def _includes_lower_case_letters(self, password):
        return self._includes_any(self.LOWER_CASE_LETTERS, password)

    def _includes_special_characters(self, password):
        return self._includes_any(self.REQUIRED_SPECIAL_CHARACTERS, password)

    @staticmethod
    def _includes_any(pattern, password):
        return re.search(pattern, password) is not None

    REQUIRED_SPECIAL_CHARACTERS = '[%#]'
    UPPER_CASE_LETTERS = '[A-Z]'
    LOWER_CASE_LETTERS = '[a-z]'
    NUMBERS = '[0-9]'
