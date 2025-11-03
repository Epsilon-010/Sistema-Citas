from ..value_objects.UserApellidoMaterno import UserApellidoMaterno
from ..value_objects.UserApellidoPaterno import UserApellidoPaterno
from ..value_objects.UserNombre import UserNombre
from ..value_objects.UserEmail import UserEmail
from ..value_objects.UserNumero import UserNumero
from ..value_objects.UserIne import UserIne
from ..value_objects.UserFechaNacimiento import UserFechaNacimiento
from ..value_objects.UserId import UserId
from typing import Optional


class User:

    def __init__(self,nombre:Optional[str] = None,apellido_paterno:Optional[str] = None,apellido_materno:Optional[str] = None
                 ,genero:Optional[str] = None,fecha_nacimiento:Optional[str] = None,ine:Optional[str] = None,correo:Optional[str] = None,numero:Optional[str] = None,id:Optional[str] = None):
        self.id = UserId(id) 
        self.nombre = UserNombre(nombre) if nombre else None
        self.apellido_paterno = UserApellidoPaterno(apellido_paterno) if apellido_paterno else None
        self.apellido_materno = UserApellidoMaterno(apellido_materno) if apellido_materno else None
        self.genero = genero
        self.fecha_nacimiento = UserFechaNacimiento(fecha_nacimiento) if fecha_nacimiento else None
        self.ine = UserIne(ine) if ine else None
        self.correo = UserEmail(correo) if correo else None
        self.numero = UserNumero(numero) if numero else None
