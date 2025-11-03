import re

class UserApellidoMaterno:

    def __init__(self,value:str):
        self._validatedApellidoMaterno(value)
        self._value = value

    @staticmethod
    def _validatedApellidoMaterno(value:str):
        if " " in value:
            raise ValueError("No puede contener espacios en blanco")
        if len(value) < 3:
            raise ValueError("No puede tener menos de 3 caracteres")
        if not value.isalpha():
            raise ValueError("No puede tener otros caracteres que no sean letras")
    @property
    def value(self):
        return self._value