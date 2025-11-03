from ...domain.repository.UserRepository import UserRepository
from ...domain.value_objects.UserApellidoMaterno import UserApellidoMaterno

class UserGetByApellidoMaterno:

    def __init__(self,repository:UserRepository):
        self.repository = repository
    
    async def run(self,apellido_materno:str):
        return await self.repository.getByApellidoMaterno(UserApellidoMaterno(apellido_materno))
    