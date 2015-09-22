import re


class PasswordValidator(object):
    def __init__(self, minimum_length):
        self.minimum_length = minimum_length

    def is_strong_password(self, password):
        return self._has_minimum_length(password) and re.search('[0-9]', password) is not None

    def _has_minimum_length(self, password):
        return len(password) >= self.minimum_length