from pydantic import BaseModel,EmailStr,Field
from ...domain.entities.User import User
from datetime import datetime

class UserDetailResponse(BaseModel):
    Nombre:str
    Apellido_Paterno:str
    Apellido_Materno:str
    Genero:str
    Fecha_Nacimiento:datetime
    Ine:str
    Correo:EmailStr
    Numero:str

    @classmethod
    def from_domain(cls, user: User):
        return cls(
            Nombre=user.nombre.value,
            Apellido_Paterno=user.apellido_paterno.value,
            Apellido_Materno=user.apellido_materno.value,
            Genero=user.genero,
            Fecha_Nacimiento=user.fecha_nacimiento.value,
            Ine=user.ine.value,
            Correo=user.correo.value,
            Numero=user.numero.value
        )

class UserFoundResponse(BaseModel):
    Nombre:str
    Apellido_Paterno:str
    Apellido_Materno:str
    Correo:EmailStr
    Numero:str

    @classmethod
    def from_domain(cls, user: User):
        return cls(
            Nombre=user.nombre.value,
            Apellido_Paterno=user.apellido_paterno.value,
            Apellido_Materno=user.apellido_materno.value,
            Correo=user.correo.value,
            Numero=user.numero.value
        )

class UserCreateRequest(BaseModel):
    Nombre: str = Field(..., min_length=1, max_length=100)
    Apellido_Paterno: str = Field(..., min_length=1, max_length=100)
    Apellido_Materno: str = Field(..., min_length=1, max_length=100)
    Genero: str = Field(..., max_length=10)
    Fecha_Nacimiento: str = Field(..., pattern=r'^\d{4}-\d{2}-\d{2}$')
    Ine: str = Field(..., min_length=13, max_length=18)
    Correo: EmailStr
    Numero: str = Field(..., min_length=10, max_length=50)

class UserUpdateRequest(BaseModel):
    Nombre: str | None = None
    Apellido_Paterno: str | None = None
    Apellido_Materno: str | None = None
    Genero: str | None = None
    Fecha_Nacimiento: str | None = None
    Ine: str | None = None 
    Correo: EmailStr | None = None 
    Numero: str | None = None