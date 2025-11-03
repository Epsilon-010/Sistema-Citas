from abc import ABC,abstractmethod
from typing import List
from ..entities.User import User
from ..value_objects.UserNombre import UserNombre
from ..value_objects.UserApellidoMaterno import UserApellidoMaterno
from ..value_objects.UserApellidoPaterno import UserApellidoPaterno
from ..value_objects.UserNumero import UserNumero
from ..value_objects.UserId import UserId


class UserRepository(ABC):

    @abstractmethod
    def created(self,user:User):
        pass

    @abstractmethod
    def getAll(self) -> List[User]:
        pass
    
    @abstractmethod
    def getByName(self,nombre:UserNombre) -> List[User]:
        pass
    
    @abstractmethod
    def getByApellidoPaterno(self,apellido_paterno:UserApellidoPaterno) -> List[User]:
        pass

    @abstractmethod
    def getByApellidoMaterno(self,apellido_materno:UserApellidoMaterno) -> List[User]:
        pass

    @abstractmethod
    def getByNumero(self,numero:UserNumero) -> User:
        pass
    
    @abstractmethod
    def update(self,id:UserId,user:User):
        pass

    @abstractmethod
    def delete(self,id:UserId):
        pass

    @abstractmethod
    def getById(self,id:UserId) -> User:
        pass

