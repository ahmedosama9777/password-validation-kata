from unittest import TestCase

from password_validator import PasswordValidator

class TestPasswordValidator(TestCase):
    def test_create_validator(self):
        password_validator = PasswordValidator()
        self.assertEqual(password_validator.validate(""), "")