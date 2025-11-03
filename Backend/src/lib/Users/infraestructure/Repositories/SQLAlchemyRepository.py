from ..database.DatabaseCofig import AsyncSessionLocal
from ...domain.repository.UserRepository import UserRepository
from ...domain.entities.User import User
from ..models.UserORM import UserORM
from sqlalchemy.future import select
from ...domain.entities.User import User
from ...domain.value_objects.UserApellidoMaterno import UserApellidoMaterno
from ...domain.value_objects.UserApellidoPaterno import UserApellidoPaterno
from ...domain.value_objects.UserId import UserId
from ...domain.value_objects.UserNumero import UserNumero
from ...domain.value_objects.UserNombre import UserNombre

class SQLAlchemy(UserRepository):
    
    def __init__(self,async_session_factory = AsyncSessionLocal):
        self._async_session_factory = async_session_factory

    
    def _to_domain(self,user_orm:UserORM):
        return User(
            nombre=user_orm.Nombre,
            apellido_paterno=user_orm.Apellido_Paterno,
            apellido_materno=user_orm.Apellido_Materno,
            genero=user_orm.Genero,
            fecha_nacimiento=str(user_orm.Fecha_Nacimiento),
            ine=user_orm.Ine,
            correo=user_orm.Correo,
            numero=user_orm.Numero,
            id=user_orm.Id  
        )

    async def created(self, user:User):
        user_orm = UserORM(
           Id=user.id.value,
           Nombre = user.nombre.value,
           Apellido_Paterno = user.apellido_paterno.value,
           Apellido_Materno = user.apellido_materno.value,
           Genero = user.genero,
           Fecha_Nacimiento = user.fecha_nacimiento.value,
           Ine = user.ine.value,
           Correo = user.correo.value, 
           Numero = user.numero.value
        )
        async with self._async_session_factory() as session:
           session.add(user_orm)
           await session.commit()
           await session.refresh(user_orm)
            
        
    
    async def getAll(self):
        async with self._async_session_factory() as session:
            result = await session.execute(select(UserORM))
            users_orm = result.scalars().all()
            users_domain = [self._to_domain(u) for u in users_orm]
            return users_domain



        
    async def getByApellidoMaterno(self, apellido_materno:UserApellidoMaterno):
        async with self._async_session_factory() as session:
            result = await session.execute(select(UserORM).filter(UserORM.Apellido_Materno == apellido_materno.value))
            users_orm = result.scalars().all()
            users_domain = [self._to_domain(u) for u in users_orm]
            return users_domain
    
    async def getByApellidoPaterno(self, apellido_paterno:UserApellidoPaterno):
        async with self._async_session_factory() as session:
            result = await session.execute(select(UserORM).filter(UserORM.Apellido_Paterno == apellido_paterno.value))
            users_orm = result.scalars().all()
            users_domain = [self._to_domain(u) for u in users_orm]
            return users_domain
    
    async def getByName(self, nombre:UserNombre):
        async with self._async_session_factory() as session:
            result = await session.execute(select(UserORM).filter(UserORM.Nombre.ilike(f"%{nombre.value}%")))
            users_orm = result.scalars().all()
            users_domain = [self._to_domain(u) for u in users_orm]
            return users_domain

    async def getByNumero(self, numero:UserNumero):
        async with self._async_session_factory() as session:
            result = await session.execute(select(UserORM).filter(UserORM.Numero == numero.value))
            user_orm = result.scalars().first()
            users_domain = self._to_domain(user_orm)
            return users_domain
    
    async def getById(self,id:UserId):
        async with self._async_session_factory() as session:
            result = await session.execute(select(UserORM).filter(UserORM.Id == id.value))
            user_orm = result.scalars().first()
            if not user_orm:
                return None
            user_domain = self._to_domain(user_orm)
            return user_domain

    async def delete(self, id:UserId):
        async with self._async_session_factory() as session:
            result = await session.execute(select(UserORM).filter(UserORM.Id == id.value))
            user = result.scalars().first()
            if user:
                await session.delete(user)
                await session.commit()
            return None
    
    async def update(self, id:UserId, user:User):
        async with self._async_session_factory() as session:
            result = await session.execute(select(UserORM).filter(UserORM.Id == id.value))
            new_user = result.scalars().first()
            if new_user:
                if user.nombre is not None:
                    new_user.Nombre = user.nombre.value
                if user.apellido_paterno is not None:
                    new_user.Apellido_Paterno = user.apellido_paterno.value
                if user.apellido_materno is not None:
                    new_user.Apellido_Materno = user.apellido_materno.value
                if user.genero is not None:
                    new_user.Genero = user.genero
                if user.fecha_nacimiento is not None:
                    new_user.Fecha_Nacimiento = user.fecha_nacimiento.value   
                if user.ine is not None:
                    new_user.Ine = user.ine.value
                if user.correo is not None:
                    new_user.Correo = user.correo.value
                if user.numero is not None:
                    new_user.Numero = user.numero.value

                await session.commit()
        
        

        
        
        