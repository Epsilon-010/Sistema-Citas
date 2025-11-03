from ...domain.repository.UserRepository import UserRepository
from ...domain.entities.User import User
from ...domain.value_objects.UserId import UserId
from typing import Optional

class UserUpdate:

    def __init__(self,repository:UserRepository):
        self.repository = repository
    
    async def run(self,id:str,nombre:Optional[str] = None,apellido_paterno:Optional[str] = None,apellido_materno:Optional[str] = None
                 ,genero:Optional[str] = None,fecha_nacimiento:Optional[str] = None,ine:Optional[str] = None,correo:Optional[str] = None,numero:Optional[str] = None):
        user = User(
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            genero=genero,
            fecha_nacimiento=fecha_nacimiento,
            ine=ine,
            correo=correo,
            numero=numero,
            id=id
        )

        return await self.repository.update(UserId(id),user)