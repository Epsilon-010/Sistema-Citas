from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column,String
from ....Users.infraestructure.database.DatabaseCofig import Base

class CarORM(Base):

    __tablename__ = 'cars'

    Id = Column(UUID(as_uuid=True),primary_key=True)
    Brand = Column(String(20),nullable=False)
    Model = Column(String(6),nullable=True)
    Color = Column(String(15),nullable=True)
    Plates = Column(String(12),nullable=False)