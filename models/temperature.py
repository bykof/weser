from sqlalchemy import Column, Float, DateTime, Integer

from models.base import Base

class Temperature(Base):
    __tablename__ = 'temperature'

    id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, unique=True, nullable=False)
