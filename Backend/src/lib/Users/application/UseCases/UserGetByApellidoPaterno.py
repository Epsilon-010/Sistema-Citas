from ...domain.repository.UserRepository import UserRepository
from ...domain.value_objects.UserApellidoPaterno import UserApellidoPaterno

class UserGetByApellidoPaterno:

    def __init__(self,repository:UserRepository):
        self.repository = repository
    
    async def run(self,apellido_paterno:str):
        return await self.repository.getByApellidoPaterno(UserApellidoPaterno(apellido_paterno))