from ...domain.repository.UserRepository import UserRepository
from ...domain.value_objects.UserId import UserId

class UserGetById:

    def __init__(self,respository:UserRepository):

        self.repository = respository
        
    async def run(self,id:str):
        return await self.repository.getById(UserId(id))
    

