from ...domian.value_objects.CarPlate import CarPlates
from ...domian.repository.CarRepository import CarRepository

class GetCarByPlates:

    def __init__(self,repository:CarRepository):
        self._repository = repository

    async def run(self,plates:str):
        return await self._repository.getCarByPlates(CarPlates(plates))
