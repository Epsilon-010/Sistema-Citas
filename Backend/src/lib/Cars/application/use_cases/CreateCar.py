from ...domian.repository.CarRepository import CarRepository
from ...domian.entities.Cars import Car


class CreateCar:

    def __init__(self,repository:CarRepository):
        self._repository = repository
    
    async def run(self,brand:str,model:str,color:str,plates:str):
        new_car = Car(
            brand=brand,
            model=model,
            color=color,
            plates=plates
        )
        return await self._repository.createCar(new_car)