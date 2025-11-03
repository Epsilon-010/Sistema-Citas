from ...domain.repository.UserRepository import UserRepository
from ...domain.entities.User import User

class UserCreate:

    def __init__(self,repository:UserRepository):
        self.repository = repository
    
    async def run(self,nombre:str,apellido_paterno:str,apellido_materno:str
                 ,genero:str,fecha_nacimiento:str,ine:str,correo:str,numero:str):
        user = User(
            nombre,
            apellido_paterno,
            apellido_materno,
            genero,
            fecha_nacimiento,
            ine,
            correo,
            numero
        )

        return await self.repository.created(user)