import re

class UserIne:
    def __init__(self, value: str):
        value = value.strip().upper()  # Elimina espacios y fuerza mayúsculas
        self._validatedIne(value)
        self._value = value

    @staticmethod
    def _validatedIne(value: str):
        if " " in value:
            raise ValueError("No puede tener espacios en blanco")
        patron = r"^[A-Z]{4}\d{6}[HM][A-Z]{2}[A-Z0-9]{4,5}$"
        if not re.match(patron, value):
            raise ValueError("Formato de INE incorrecto")

    @property
    def value(self):
        return self._value


        