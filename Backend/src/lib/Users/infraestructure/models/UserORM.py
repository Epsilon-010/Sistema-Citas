from sqlalchemy import Column,String,Date
from sqlalchemy.dialects.postgresql import UUID
from ..database.DatabaseCofig import Base


class UserORM(Base):

    __tablename__ = "users"

    Id = Column(UUID(as_uuid=True),primary_key=True)
    Nombre = Column(String(100),nullable=False,index=True)
    Apellido_Paterno = Column(String(100),nullable=False)
    Apellido_Materno = Column(String(100),nullable=False)
    Genero = Column(String(10),nullable=False)
    Fecha_Nacimiento = Column(Date,nullable=False,index=True)
    Ine = Column(String(18),nullable=False,unique=True)
    Correo = Column(String(100),nullable=False,unique=True,index=True)
    Numero = Column(String(50),nullable=False)
    

