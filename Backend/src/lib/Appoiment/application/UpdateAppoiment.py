from ..domain.repository.AppoimentRepository import AppoimentRepository
from ..domain.entities.Appoiment import Appoiment


class UpdateAppoiment:

    def __init__(self,repository:AppoimentRepository):
        self._reposiroty = repository

    async def run(self,id:str,fecha:str,hora:str,visitado:str,area:str,nombre:str,apellido_paterno:str,apellido_materno:str,plates:str):
        appoiment = Appoiment(
            id=id,
            fecha=fecha,
            hora=hora,
            visitado=visitado,
            area=area
        )
        return await self._reposiroty.update_appoiment(id,appoiment,nombre,apellido_paterno,apellido_materno,plates)