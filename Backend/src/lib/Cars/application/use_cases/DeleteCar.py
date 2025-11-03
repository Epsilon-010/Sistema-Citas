from ...domian.repository.CarRepository import CarRepository
from ...domian.value_objects.CarId import CarId

class DeleteCar:

    def __init__(self,repository:CarRepository):
        self._repository = repository
    
    async def run(self,id:str):
        return await self._repository.deleteCar(CarId(id))

    
