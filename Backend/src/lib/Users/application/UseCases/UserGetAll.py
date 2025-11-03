from ...domain.repository.UserRepository import UserRepository

class UserGetAll:

    def __init__(self,repository:UserRepository):
        self.repository = repository
    
    async def run(self):
        return await self.repository.getAll()