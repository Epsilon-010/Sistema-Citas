from ...domian.value_objects.CarId import CarId
from ...domian.repository.CarRepository import CarRepository


class GetCarById:

    def __init__(self,repository:CarRepository):
        self._repository = repository
    
    async def run(self,id:str):
        return self._repository.getCarById(CarId(id))

