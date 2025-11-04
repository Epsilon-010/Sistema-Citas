from ...Appoiment.application.CreateAppoiment import CreateAppoiment
from ...Appoiment.application.UpdateAppoiment import UpdateAppoiment
from ...Appoiment.application.GetAppoimentByArea import GetAppoimentByArea
from ...Appoiment.application.GetAppoimentByDate import GetAppoimentByDate
from ...Appoiment.application.GetAppoimentByVisitado import GetAppoimentByVisitado
from ...Appoiment.application.GetAppoimentByVisitante import GetAppoimentByVisitante
from ...Appoiment.application.GetAppoiments import GetAppoiments
from ...Appoiment.infraestrcuture.repository.SQLAlchemyRepository import SQLAlchemyRepository
from fastapi import Depends

class AppoimnetServiceContainer:

    @staticmethod
    def get_repository():
        return SQLAlchemyRepository()
    
    @staticmethod
    def create_appoiment(reposiroty = Depends(get_repository)):
        return CreateAppoiment(reposiroty)
    
    @staticmethod
    def update_appoiment(reposiroty = Depends(get_repository)):
        return UpdateAppoiment(reposiroty)
    
    @staticmethod
    def get_by_Area(reposiroty = Depends(get_repository)):
        return GetAppoimentByArea(reposiroty)
    
    @staticmethod
    def get_by_date(reposiroty = Depends(get_repository)):
        return GetAppoimentByDate(reposiroty)
    
    @staticmethod
    def get_by_visitado(reposiroty = Depends(get_repository)):
        return GetAppoimentByVisitado(reposiroty)
    
    @staticmethod
    def get_by_visitante(reposiroty = Depends(get_repository)):
        return GetAppoimentByVisitante(reposiroty)
    
    @staticmethod
    def get_appoiments(reposiroty = Depends(get_repository)):
        return GetAppoiments(reposiroty)
    
    

    
