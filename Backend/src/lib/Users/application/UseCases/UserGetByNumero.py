from ...domain.repository.UserRepository import UserRepository
from ...domain.value_objects.UserNumero import UserNumero

class UserGetByNumero:

    def __init__(self,repository:UserRepository):
        self.repository = repository
    
    async def run(self,numero:str):
        return await self.repository.getByNumero(UserNumero(numero))