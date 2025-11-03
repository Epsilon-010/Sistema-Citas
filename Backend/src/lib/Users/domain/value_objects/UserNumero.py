import re

class UserNumero:

    def __init__(self,value:str):
        self._validatedNumero(value)
        self._value = value


    @staticmethod
    def _validatedNumero(value:str):
        
        if not value.isdigit():
            raise ValueError(f"No puede contener caracteres que no sean numeros")
        if len(value) < 10:
            raise ValueError(f"No puede ser menor a 10 digitos")
        
    @property
    def value(self):
        return self._value