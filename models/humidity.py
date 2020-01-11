from sqlalchemy import Column, Float, DateTime, Integer

from models.base import Base

class Humidity(Base):
    __tablename__ = 'humidity'

    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, unique=True, nullable=False)
