from ...domain.entities.Appoiment import Appoiment
from ...domain.repository.AppoimentRepository import AppoimentRepository
from ....Users.infraestructure.database.DatabaseCofig import AsyncSessionLocal
from ..models.AppoimentORM import AppoimentORM
from ....Users.infraestructure.models.UserORM import UserORM
from ....Cars.infraestrcuture.models.CarORM import CarORM
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload



class SQLAlchemyRepository(AppoimentRepository):
    
    def __init__(self,async_session_factory = AsyncSessionLocal):
        self._async_session_factory = async_session_factory

    async def create_appoiment(self, appoiment:Appoiment,nombre:str,apellido_paterno:str,apellido_materno:str,plates:str = None):
         async with self._async_session_factory() as session:
            car = None
            filtrosUser = []
            if nombre:
                filtrosUser.append(UserORM.Nombre == nombre)
            if apellido_paterno:
                filtrosUser.append(UserORM.Apellido_Paterno == apellido_paterno)
            if apellido_materno:
                filtrosUser.append(UserORM.Apellido_Materno == apellido_materno)
           
            resultUser = await session.execute(select(UserORM).where(*filtrosUser))
            user = resultUser.scalars().first()
            if plates:
                resultCar = await session.execute(select(CarORM).where(CarORM.Plates == plates))
                car = resultCar.scalars().first()

            new_appoiment_orm = AppoimentORM(

                Id = appoiment.id.value,
                Id_Visitante = user.Id,
                Car_Id = car.Id if car else None,
                Fecha = appoiment.fecha,
                Hora = appoiment.hora,
                Visitado = appoiment.visitado,
                Area = appoiment.area
            )

            session.add(new_appoiment_orm)
            await session.commit()
            await session.refresh(new_appoiment_orm)
    
    async def get_appoiments(self):
        async with self._async_session_factory() as session:
            results = await session.execute(select(AppoimentORM).options(
                selectinload(AppoimentORM.visitante),
                selectinload(AppoimentORM.car)
            ))
            appoimnets = results.scalars().all()
            return appoimnets
    
    async def get_appoiment_by_area(self, area):
        async with self._async_session_factory() as session:
            results = await session.execute(select(AppoimentORM).options(
                selectinload(AppoimentORM.visitante),
                selectinload(AppoimentORM.car)
            ).where(AppoimentORM.Area == area))
            appoimnets = results.scalars().all()
            return appoimnets
    
    async def get_appoiment_by_visitado(self, visitado):
        async with self._async_session_factory() as session:
            results = await session.execute(select(AppoimentORM).options(
                selectinload(AppoimentORM.visitante),
                selectinload(AppoimentORM.car)
            ).where(AppoimentORM.Visitado == visitado))
            appoimnets = results.scalars().all()
            return appoimnets
        
    async def get_appoiment_by_date(self, fecha):
        async with self._async_session_factory() as session:
            results = await session.execute(select(AppoimentORM).options(
                selectinload(AppoimentORM.visitante),
                selectinload(AppoimentORM.car)
            ).where(AppoimentORM.Fecha == fecha))
            appoimnets = results.scalars().all()
            return appoimnets
    
    async def get_appoiment_by_visitante(self, nombre:str,apellido_paterno:str,apellido_materno:str):
        async with self._async_session_factory() as session:
            filtrosUser = []
            if nombre:
                filtrosUser.append(UserORM.Nombre == nombre)
            if apellido_paterno:
                filtrosUser.append(UserORM.Apellido_Paterno == apellido_paterno)
            if apellido_materno:
                filtrosUser.append(UserORM.Apellido_Materno == apellido_materno)
           
            resultUser = await session.execute(select(UserORM).where(*filtrosUser))
            user = resultUser.scalars().first()

            results = await session.execute(select(AppoimentORM).options(
                selectinload(AppoimentORM.visitante),
                selectinload(AppoimentORM.car)
            ).where(AppoimentORM.Id_Visitante == user.Id))
            appoimnets = results.scalars().all()
            return appoimnets

    async def update_appoiment(self, id, appoiment:Appoiment,nombre:str,apellido_paterno:str,apellido_materno:str,plates:str):
        async with self._async_session_factory() as session:
            filtrosUser = []
            if nombre:
                filtrosUser.append(UserORM.Nombre == nombre)
            if apellido_paterno:
                filtrosUser.append(UserORM.Apellido_Paterno == apellido_paterno)
            if apellido_materno:
                filtrosUser.append(UserORM.Apellido_Materno == apellido_materno)
           
            resultUser = await session.execute(select(UserORM).where(*filtrosUser))
            user = resultUser.scalars().first()
            if plates:
                resultCar = await session.execute(select(CarORM).where(CarORM.Plates == plates))
                car = resultCar.scalars().first()
            resultUpdate = session.execute(select(AppoimentORM).where(AppoimentORM.Id == id))
            update_appoiment = resultUpdate.scalars().first()
            if update_appoiment:
                if appoiment.area is not None:
                    update_appoiment.Area = appoiment.area
                if appoiment.hora is not None:
                    update_appoiment.Hora = appoiment.hora
                if appoiment.fecha is not None:
                    update_appoiment.Fecha = appoiment.fecha
                if appoiment.visitado is not None:
                    update_appoiment.Visitado = appoiment.visitado
                if user:
                    update_appoiment.Id_Visitante = user.Id
                if car:
                    update_appoiment.Car_Id = car.Id
                    


            
           


        
