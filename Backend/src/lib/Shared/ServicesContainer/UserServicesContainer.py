from ...Users.infraestructure.Repositories.SQLAlchemyRepository import SQLAlchemy
from ...Users.application.UseCases.UserGetAll import UserGetAll
from ...Users.application.UseCases.UserCreate import UserCreate
from ...Users.application.UseCases.UserDelete import UserDelete
from ...Users.application.UseCases.UserGetByApellidoMaterno import UserGetByApellidoMaterno
from ...Users.application.UseCases.UserGetByApellidoPaterno import UserGetByApellidoPaterno
from ...Users.application.UseCases.UserGetByName import UserGetByName
from ...Users.application.UseCases.UserGetByNumero import UserGetByNumero
from ...Users.application.UseCases.UserUpdate import UserUpdate
from ...Users.application.UseCases.UserGetById import UserGetById
from fastapi import Depends

class UserServiceContainer:

    @staticmethod
    def get_repository():
        return SQLAlchemy()

    @staticmethod
    def getAllUsers(Repository:SQLAlchemy = Depends(get_repository)):
        return UserGetAll(Repository)
    
    @staticmethod
    def updateUser(Repository:SQLAlchemy = Depends(get_repository)):
        return UserUpdate(Repository)
    
    @staticmethod
    def deleteUser(Repository:SQLAlchemy = Depends(get_repository)):
        return UserDelete(Repository)
    
    @staticmethod
    def getUserByName(Repository:SQLAlchemy = Depends(get_repository)):
        return UserGetByName(Repository)
    
    @staticmethod
    def getUserByApellidoPaterno(Repository:SQLAlchemy = Depends(get_repository)):
        return UserGetByApellidoPaterno(Repository)
    
    @staticmethod
    def getUserByApellidoMaterno(Repository:SQLAlchemy = Depends(get_repository)):
        return UserGetByApellidoMaterno(Repository)
    
    @staticmethod
    def createUser(Repository:SQLAlchemy = Depends(get_repository)):
        return UserCreate(Repository)
    
    @staticmethod
    def getUserByNumero(Repository:SQLAlchemy = Depends(get_repository)):
        return UserGetByNumero(Repository)
    
    @staticmethod
    def getUserById(Respository:SQLAlchemy = Depends(get_repository)):
        return UserGetById(Respository)