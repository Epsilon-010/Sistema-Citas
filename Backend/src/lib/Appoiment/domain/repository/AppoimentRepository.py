from abc import ABC,abstractmethod
from ..entities.Appoiment import Appoiment

class AppoimentRepository(ABC):

    @abstractmethod
    def get_appoiments(self):
        pass

    def get_appoiment_by_date(self,fecha:str):
        pass

    def get_appoiment_by_visitante(self,nombre:str,apellido_paterno:str,apellido_materno:str):
        pass

    def get_appoiment_by_visitado(self,visitado:str):
        pass

    def get_appoiment_by_area(self,area:str):
        pass

    def update_appoiment(self,id,appoiment:Appoiment,nombre:str,apellido_paterno:str,apellido_materno:str,plates:str):
        pass

    def create_appoiment(self,appoiment:Appoiment,nombre:str,apellido_paterno:str,apellido_materno:str,plate:str):
        pass