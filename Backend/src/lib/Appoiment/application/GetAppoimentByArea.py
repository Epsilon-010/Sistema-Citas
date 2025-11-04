from ..domain.repository.AppoimentRepository import AppoimentRepository


class GetAppoimentByArea:

    def __init__(self,repository:AppoimentRepository):
        self._reposiroty = repository

    async def run(self,area:str):
        return await self._reposiroty.get_appoiment_by_area(area)