from datetime import datetime


class UserFechaNacimiento:

    def __init__(self,value:str):

        self._value = self._validate_fecha(value)

    @staticmethod
    def _validate_fecha(value: str):
        try:
            return datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD")

    @property
    def value(self):
        return self._value        
