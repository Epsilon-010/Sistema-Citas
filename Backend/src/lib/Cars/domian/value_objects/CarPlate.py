import re 

class CarPlates:

    def __init__(self,value:str):
        if not self.check_plate(value):
            raise ValueError("Formato de placas incorrecto")
        self._value = value

    @staticmethod
    def check_plate(value:str):
        patron = r"^[A-Z]{1,3}-?\d{1,4}-?[A-Z]{0,3}$"
        return bool(re.match(patron,value))

    @property
    def value(self):
        return self._value
        