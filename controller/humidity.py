from typing import Union

from sqlalchemy.orm import Session

from models.humidity import Humidity
from api_schemas.humidity import HumidityCreate, Humidity as HumiditySchema


class HumidityController:
    def create(db: Session, humidity_create: HumidityCreate) -> Humidity:
        humidity = Humidity(**humidity_create.dict())
        db.add(humidity)
        db.commit()
        db.refresh(humidity)
        return humidity

    def get_one(db: Session, id: int) -> Union[Humidity, None]:
        return db.query(Humidity).filter(Humidity.id == id).first()

    def delete(db: Session, id: int) -> None:
        humidity = db.query(Humidity).filter(Humidity.id == id).first()
        if humidity:
            db.delete(humidity)
        db.commit()
