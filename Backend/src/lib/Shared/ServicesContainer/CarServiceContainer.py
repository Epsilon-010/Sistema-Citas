from ...Cars.application.use_cases.CreateCar import CreateCar
from ...Cars.application.use_cases.UpdateCar import UpdateCar
from ...Cars.application.use_cases.DeleteCar import DeleteCar
from ...Cars.application.use_cases.GetAllCars import GetAllCars
from ...Cars.application.use_cases.GetCarById import GetCarById
from ...Cars.application.use_cases.GetCarByPlates import GetCarByPlates
from ...Cars.infraestrcuture.reposirories.SQLAlchemyRepository import SQLAlchemyReposiroty
from fastapi import Depends

class CarServiceContainer:

    @staticmethod
    def get_repository():
        return SQLAlchemyReposiroty()
    
    @staticmethod
    def create_car(repository = Depends(get_repository)):
        return CreateCar(repository)
    
    @staticmethod
    def update_car(reposiroty = Depends(get_repository)):
        return UpdateCar(reposiroty)
    
    @staticmethod
    def delete_car(repository = Depends(get_repository)):
        return DeleteCar(repository)
    
    @staticmethod
    def get_all_cars(repository = Depends(get_repository)):
        return GetAllCars(repository)
    
    @staticmethod
    def get_car_by_id(repository = Depends(get_repository)):
        return GetCarById(repository)
    
    @staticmethod
    def get_car_by_plates(repository = Depends(get_repository)):
        return GetCarByPlates(repository)
