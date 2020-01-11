from typing import List

import datetime

from pydantic import BaseModel


class TemperatureBase(BaseModel):
    value: float
    timestamp: datetime.datetime

    class Config:
        orm_mode = True


class TemperatureCreate(TemperatureBase):
    pass


class Temperature(TemperatureBase):
    id: int
