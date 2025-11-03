from ...domain.repository.UserRepository import UserRepository
from ...domain.value_objects.UserId import UserId

class UserDelete:

    def __init__(self,repository:UserRepository):
        self.repository = repository
    
    async def run(self,id:str):
        return await self.repository.delete(UserId(id))