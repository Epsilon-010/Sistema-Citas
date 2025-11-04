from ..value_objects.CarBrand import CarBrand
from ..value_objects.CarColor import CarColor
from ..value_objects.CarPlate import CarPlates
from ..value_objects.CarModel import CarModel
from ..value_objects.CarId import CarId
from typing import Optional

class Car:

    def __init__(self,id:Optional[str] = None,brand:Optional[str] = None,model:Optional[str] = None,color:Optional[str] = None,plates:Optional[str] = None):
        
        self.id = CarId(id)
        self.brand = CarBrand(brand) if brand else None
        self.model = CarModel(model) if model else None
        self.color = CarColor(color) if color else None
        self.plates = CarPlates(plates) if plates else None



        