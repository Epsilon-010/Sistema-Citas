from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class UserSchema(BaseModel):
    Nombre: str
    Apellido_Paterno: str
    Apellido_Materno: str

    class Config:
        from_attributes = True 


class CarSchema(BaseModel):
    Brand: str
    Plates: str
    Color: Optional[str] = None

    class Config:
        from_attributes = True


class AppointmentSchema(BaseModel):
    Fecha: date
    Hora: time
    Visitado: str
    Area: str
    visitante: UserSchema
    car: Optional[CarSchema] = None

    class Config:
        from_attributes = True

class CreateAppoimentSchema(BaseModel):
    fecha: date
    hora: time
    visitado: str
    area: str
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    plates: Optional[str] = None

    class Config:
        orm_mode = True


class FoundVisitor(BaseModel):
    nombre : str
    apellido_paterno:str
    apellido_materno:str

    class Config:
        orm_mode = True
