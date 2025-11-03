from ...domain.repository.UserRepository import UserRepository
from ...domain.value_objects.UserNombre import UserNombre

class UserGetByName:

    def __init__(self,repository:UserRepository):
        self.repository = repository
    
    async def run(self,nombre:str):
        return await self.repository.getByName(UserNombre(nombre))