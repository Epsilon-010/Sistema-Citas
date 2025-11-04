from ...domian.repository.CarRepository import CarRepository
from ....Users.infraestructure.database.DatabaseCofig import AsyncSessionLocal
from ..models.CarORM import CarORM
from ...domian.entities.Cars import Car
from sqlalchemy.future import select
from ...domian.value_objects.CarId import CarId
from ...domian.value_objects.CarPlate import CarPlates

class SQLAlchemyReposiroty(CarRepository):

    def __init__(self,async_session_factory = AsyncSessionLocal):
        self._async_session_factory = async_session_factory

    def _to_domain(self,car_orm:CarORM):
        return Car(
            id=car_orm.Id,
            brand=car_orm.Brand,
            model=car_orm.Model,
            color=car_orm.Color,
            plates=car_orm.Plates
        )
    
    async def createCar(self, car:Car):
        car_orm = CarORM(
            Id = car.id.value,
            Brand = car.brand.value,
            Model = car.model.value,
            Color = car.color.value,
            Plates = car.plates.value
        )
        async with self._async_session_factory() as session:
            session.add(car_orm)
            await session.commit()
            await session.refresh(car_orm)

    async def updateCar(self, id:CarId, car:Car):
        async with self._async_session_factory() as session:
            result = await session.execute(select(CarORM).filter(CarORM.Id == id.value))
            update_car = result.scalars().first()

            if update_car:
                if car.brand is not None:
                    update_car.Brand = car.brand.value
                if car.color is not None:
                    update_car.Color = car.color.value
                if car.model is not None:
                    update_car.Model = car.model.value
                if car.plates is not None:
                    update_car.Plates = car.plates.value
                await session.commit()
                return True
            else:
                return False
    
    async def deleteCar(self, id:CarId):
        async with self._async_session_factory() as session:
            result = await session.execute(select(CarORM).filter(CarORM.Id == id.value))
            car_delete = result.scalars().first()
            
            if car_delete:
                await session.delete(car_delete)
                await session.commit()
                return True
            else:
                return False
    
    async def getAllCars(self):
        async with self._async_session_factory() as session:
            results = await session.execute(select(CarORM))
            users_orm = results.scalars().all()
            users_domain = [self._to_domain(user) for user in users_orm]
            return users_domain
    
    async def getCarById(self, id:CarId):
        async with self._async_session_factory() as session:
            result = await session.execute(select(CarORM).filter(CarORM.Id == id.value))
            user_orm = result.scalars().first()
            user_domain = self._to_domain(user_orm)
            return user_domain
    
    async def getCarByPlates(self, plates:CarPlates):
        async with self._async_session_factory() as session:
            result = await session.execute(select(CarORM).filter(CarORM.Plates == plates.value))
            user_orm = result.scalars().first()
            user_domain = self._to_domain(user_orm)
            return user_domain

        
            
    
