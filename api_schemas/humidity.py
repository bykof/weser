from typing import List

import datetime

from pydantic import BaseModel


class HumidityBase(BaseModel):
    value: float
    timestamp: datetime.datetime

    class Config:
        orm_mode = True


class HumidityCreate(HumidityBase):
    pass


class Humidity(HumidityBase):
    id: int
