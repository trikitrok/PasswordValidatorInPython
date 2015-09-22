import re


class PasswordValidator(object):
    def __init__(self, minimum_length):
        self.minimum_length = minimum_length

    def is_strong_password(self, password):
        includes_numbers = self._includes_numbers(password)
        has_minimum_length = self._has_minimum_length(password)
        return has_minimum_length and includes_numbers

    def _has_minimum_length(self, password):
        return len(password) >= self.minimum_length

    def _includes_numbers(self, password):
        return re.search('[0-9]', password) is not None