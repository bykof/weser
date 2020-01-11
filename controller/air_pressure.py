from typing import Union

from sqlalchemy.orm import Session

from models.air_pressure import AirPressure
from api_schemas.air_pressure import AirPressureCreate, AirPressure as AirPressureSchema


class AirPressureController:
    def create(db: Session, air_pressure_create: AirPressureCreate) -> AirPressure:
        air_pressure = AirPressure(**air_pressure_create.dict())
        db.add(air_pressure)
        db.commit()
        db.refresh(air_pressure)
        return air_pressure

    def get_one(db: Session, id: int) -> Union[AirPressure, None]:
        return db.query(AirPressure).filter(AirPressure.id == id).first()

    def delete(db: Session, id: int) -> None:
        air_pressure = db.query(AirPressure).filter(AirPressure.id == id).first()
        if air_pressure:
            db.delete(air_pressure)
        db.commit()
