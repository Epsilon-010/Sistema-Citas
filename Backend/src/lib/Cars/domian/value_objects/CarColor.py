class CarColor:

    def __init__(self,value:str):
        self.check_color(value)
        self._value = value

    @staticmethod
    def check_color(value:str):
        if " " in value:
            raise ValueError("La propiedad color no puede tener espacios")
        if  not value.isalpha():
            raise ValueError("La propiedad color no puede tener numeros")
        if len(value) < 3:
            raise ValueError("La propiedad color no puede ser menor a 3 caracteres")
    
    @property
    def value(self):
        return self._value

    
