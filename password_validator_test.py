from unittest import TestCase

from password_validator import PasswordValidator


class TestPasswordValidator(TestCase):
    def test_validate_password_is_atleast_eight_chars_long(self):
        password_validator = PasswordValidator(password="Qw*r12")
        valid, error_string = password_validator.validate()
        self.assertEqual(valid, False)
        self.assertEqual(error_string, "\nPassword must be at least 8 charachters")

    def test_validate_password_contains_two_or_more_numbers(self):
        password_validator = PasswordValidator(password="1qwer*Tyu")
        valid, error_string = password_validator.validate()
        self.assertEqual(valid, False)
        self.assertEqual(error_string, "\nThe password must contain at least 2 numbers")

    def test_handle_multiple_validation_errors(self):
        password_validator = PasswordValidator(password="qQ*er")
        valid, error_string = password_validator.validate()
        self.assertEqual(valid, False)
        self.assertEqual(
            error_string,
            "\nPassword must be at least 8 charachters\nThe password must contain at least 2 numbers",
        )

    def test_validate_password_contains_one_or_more_capital_letter(self):
        password_validator = PasswordValidator(password="qwe*rty12")
        valid, error_string = password_validator.validate()
        self.assertEqual(valid, False)
        self.assertEqual(error_string, "\nThe password must contain at least 1 capital letter")
    
    def test_validate_password_contains_one_or_more_special_chars(self):
        password_validator = PasswordValidator(password="Qwerty12")
        valid, error_string = password_validator.validate()
        self.assertEqual(valid, False)
        self.assertEqual(error_string, "\nThe password must contain at least 1 special charachter")
    
    def test_perfect_password(self):
        password_validator = PasswordValidator(password="Qwer*ty12")
        valid, error_string = password_validator.validate()
        self.assertEqual(valid, True)
        self.assertEqual(error_string, "")