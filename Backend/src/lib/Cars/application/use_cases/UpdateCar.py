from ...domian.repository.CarRepository import CarRepository
from ...domian.entities.Cars import Car
from typing import Optional
from ...domian.value_objects.CarId import CarId


class UpdateCar:

    def __init__(self,repository:CarRepository):
        self._repository = repository

    async def run(self,id:str,brand:Optional[str] = None,model:Optional[str] = None,color:Optional[str] = None,plates:Optional[str] = None):
        update_car = Car(
            id=id,
            brand=brand,
            model=model,
            color=color,
            plates=plates
        )

        return await self._repository.updateCar(CarId(id),update_car)