from ..domain.repository.AppoimentRepository import AppoimentRepository


class GetAppoiments:

    def __init__(self,repository:AppoimentRepository):
        self._reposiroty = repository

    async def run(self):
        return await self._reposiroty.get_appoiments()