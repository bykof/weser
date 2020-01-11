from typing import Union

from sqlalchemy.orm import Session

from models.temperature import Temperature
from api_schemas.temperature import TemperatureCreate


class TemperatureController:
    def create(db: Session, temperature_create: TemperatureCreate) -> Temperature:
        temperature = Temperature(**temperature_create.dict())
        db.add(temperature)
        db.commit()
        db.refresh(temperature)
        return temperature

    def get_one(db: Session, id: int) -> Union[Temperature, None]:
        return db.query(Temperature).filter(Temperature.id == id).first()

    def delete(db: Session, id: int) -> None:
        temperature = db.query(Temperature).filter(
            Temperature.id == id
        ).first()
        if temperature:
            db.delete(temperature)
        db.commit()
