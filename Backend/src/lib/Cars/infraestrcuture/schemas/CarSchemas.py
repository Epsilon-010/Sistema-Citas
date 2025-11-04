from pydantic import BaseModel
from ...domian.entities.Cars import Car

class CarBase(BaseModel):
    Brand: str | None = None
    Model: str | None = None
    Color: str | None = None
    Plates: str | None = None

    @staticmethod
    def from_domain(car:Car):
        if not car:
            return None  
        return CarBase(
            Brand=car.brand.value if car.brand else None,
            Model=car.model.value if car.model else None,
            Color=car.color.value if car.color else None,
            Plates=car.plates.value if car.plates else None
        )

