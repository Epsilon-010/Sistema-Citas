from ...domian.repository.CarRepository import CarRepository

class GetAllCars:

    def __init__(self,repository:CarRepository):
        self._repository = repository
    
    async def run(self):
        return await self._repository.getAllCars()