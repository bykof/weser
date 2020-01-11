from sqlalchemy import Column, Float, DateTime, Integer

from models.base import Base

class AirPressure(Base):
    __tablename__ = 'air_pressure'

    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, unique=True, nullable=False)
