class PasswordValidator:
    def __init__(self, password: str):
        self.password = password

    def validate(self):
        error_string = ""

        if not self._more_than_eight_charachters():
            error_string += "\n" + "Password must be at least 8 charachters"

        if not self._has_two_numbers():
            error_string += "\n" + "The password must contain at least 2 numbers"
        
        if not self._has_one_capital_letter():
            error_string += "\n" + "The password must contain at least 1 capital letter"

        return False if error_string else True, error_string

    def _more_than_eight_charachters(self):
        if len(self.password) < 8:
            return False

        return True

    def _has_two_numbers(self):
        numbers = 0
        for char in self.password:
            if char.isnumeric():
                numbers += 1
        if numbers < 2:
            return False

        return True

    def _has_one_capital_letter(self):
        for char in self.password:
            if char.isupper():
                return True
        
        return False