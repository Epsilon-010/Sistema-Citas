from ..domain.repository.AppoimentRepository import AppoimentRepository
from ..domain.entities.Appoiment import Appoiment

class GetAppoimentByDate:

    def __init__(self,repository:AppoimentRepository):
        self._reposiroty = repository

    async def run(self,fecha:str):
        return await self._reposiroty.get_appoiment_by_date(fecha)