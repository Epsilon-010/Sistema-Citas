import re

class UserEmail:

    def __init__(self,value:str):
        if not self._validatedEmail(value):
            raise ValueError(f"Email invalido")
        self._value = value.lower().strip()

    @staticmethod
    def _validatedEmail(value:str) -> bool:
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(patron,value))
    
    @property
    def value(self):
        return self._value
