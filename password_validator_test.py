from unittest import TestCase

from password_validator import PasswordValidator


class TestPasswordValidator(TestCase):
    def test_validate_password_is_atleast_eight_chars_long(self):
        password_validator = PasswordValidator(password="Qwer12")
        valid, error_string = password_validator.validate()
        self.assertEqual(valid, False)
        self.assertEqual(error_string, "\nPassword must be at least 8 charachters")

    def test_validate_password_contains_two_or_more_numbers(self):
        password_validator = PasswordValidator(password="1qwerTyu")
        valid, error_string = password_validator.validate()
        self.assertEqual(valid, False)
        self.assertEqual(error_string, "\nThe password must contain at least 2 numbers")

    def test_handle_multiple_validation_errors(self):
        password_validator = PasswordValidator(password="qQer")
        valid, error_string = password_validator.validate()
        self.assertEqual(valid, False)
        self.assertEqual(
            error_string,
            "\nPassword must be at least 8 charachters\nThe password must contain at least 2 numbers",
        )

    def test_validate_password_contains_one_or_more_capital_letter(self):
        password_validator = PasswordValidator(password="qwerty12")
        valid, error_string = password_validator.validate()
        self.assertEqual(valid, False)
        self.assertEqual(error_string, "\nThe password must contain at least 1 capital letter")