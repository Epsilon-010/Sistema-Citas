from ..domain.repository.AppoimentRepository import AppoimentRepository


class GetAppoimentByVisitado:

    def __init__(self,repository:AppoimentRepository):
        self._reposiroty = repository

    async def run(self,visitado:str):
        return await self._reposiroty.get_appoiment_by_visitado(visitado)