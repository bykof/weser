from typing import List

import datetime

from pydantic import BaseModel


class AirPressureBase(BaseModel):
    value: float
    timestamp: datetime.datetime

    class Config:
        orm_mode = True


class AirPressureCreate(AirPressureBase):
    pass


class AirPressure(AirPressureBase):
    id: int
