class CarModel:

    def __init__(self,value:str):
        self.check_model(value)
        self._value = value

    @staticmethod
    def check_model(value:str):
        if " " in value:
            raise ValueError("La propiedad modelo no puede tener espacios")
        if  not value.isdigit():
            raise ValueError("La propiedad modelo no puede tener letras")
        if len(value) != 4:
            raise ValueError("La propiedad marca solo puede tener 4 caracteres")
    
    @property
    def value(self):
        return self._value