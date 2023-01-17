from unittest import TestCase

from password_validator import PasswordValidator

class TestPasswordValidator(TestCase):
    def test_validate_password_is_atleast_eight_chars_long(self):
        password_validator = PasswordValidator()
        error_string = password_validator.validate("qwer")
        self.assertEqual(error_string, "Password must be at least 8 charachters")