from ....Users.infraestructure.database.DatabaseCofig import Base
from sqlalchemy import Column,String,ForeignKey,Date,Time
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship



class AppoimentORM(Base):

    __tablename__ = 'citas'
    Id = Column(UUID(as_uuid=True),primary_key=True)
    Id_Visitante = Column(UUID(as_uuid=True), ForeignKey('users.Id'),nullable=False)
    Car_Id = Column(UUID(as_uuid=True), ForeignKey('cars.Id'),nullable=True)
    Fecha = Column(Date,nullable=False)
    Hora = Column(Time,nullable=False)
    Visitado = Column(String(30),nullable=False)
    Area = Column(String(30),nullable=False)

    visitante = relationship("UserORM", back_populates="citas")
    car = relationship("CarORM", back_populates="citas")