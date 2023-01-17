class PasswordValidator():
    def validate(self, password: str):
        error_string = ""
        
        if len(password) < 8:
            error_string = "Password must be at least 8 charachters"
        
        return error_string