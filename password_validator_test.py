from unittest import TestCase

from password_validator import PasswordValidator


class TestPasswordValidator(TestCase):
    def test_validate_password_is_atleast_eight_chars_long(self):
        password_validator = PasswordValidator(password="qwer")
        error_string = password_validator.validate()
        self.assertEqual(error_string, "Password must be at least 8 charachters")

    def test_validate_password_contains_two_or_more_numbers(self):
        password_validator = PasswordValidator(password="1qwertyu")
        error_string = password_validator.validate()
        self.assertEqual(error_string, "The password must contain at least 2 numbers")
