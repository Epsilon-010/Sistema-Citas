from abc import ABC,abstractmethod
from ..entities.Cars import Car
from typing import List
from ..value_objects.CarId import CarId
from ..value_objects.CarPlate import CarPlates




class CarRepository(ABC):

    @abstractmethod
    def createCar(self,car:Car):
        pass

    @abstractmethod
    def updateCar(self,id:CarId,car:Car):
        pass

    @abstractmethod
    def deleteCar(self,id:CarId):
        pass
    
    @abstractmethod
    def getAllCars(self) -> List[Car]:
        pass
    
    @abstractmethod
    def getCarByPlates(self,paltes:CarPlates) -> Car:
        pass

    @abstractmethod
    def getCarById(self,id:CarId):
        pass