from ..domain.repository.AppoimentRepository import AppoimentRepository


class GetAppoimentByVisitante:

    def __init__(self,repository:AppoimentRepository):
        self._reposiroty = repository

    async def run(self,nombre:str,apellido_paterno:str,apellido_materno:str):
        return await self._reposiroty.get_appoiment_by_visitante(nombre,apellido_paterno,apellido_materno)