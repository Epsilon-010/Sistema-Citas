class CarBrand:

    def __init__(self,value:str):
        self.check_brand(value)
        self._value = value

    @staticmethod
    def check_brand(value:str):
        if " " in value:
            raise ValueError("La propiedad marca no puede tener espacios")
        if  not value.isalpha():
            raise ValueError("La propiedad marca no puede tener numeros")
        if len(value) < 3:
            raise ValueError("La propiedad marca no puede ser menor a 3 caracteres")
    
    @property
    def value(self):
        return self._value