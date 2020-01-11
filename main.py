from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database.session import LocalSession

from api_schemas.air_pressure import AirPressure, AirPressureCreate
from api_schemas.humidity import Humidity, HumidityCreate
from api_schemas.temperature import Temperature, TemperatureCreate

from controller.air_pressure import AirPressureController
from controller.humidity import HumidityController
from controller.temperature import TemperatureController


def get_db():
    try:
        db = LocalSession()
        yield db
    finally:
        db.close()


app = FastAPI(title='Weser', description='A weather statistics tracker')


@app.post('/temperature/', response_model=Temperature, tags=['Temperature'])
def create_temperature(temperature: TemperatureCreate, db: Session = Depends(get_db)):
    return TemperatureController.create(db, temperature)


@app.get('/temperature/{id}', response_model=Temperature, tags=['Temperature'])
def get_temperature(id: int, db: Session = Depends(get_db)):
    temperature = TemperatureController.get_one(db, id)
    if temperature is None:
        raise HTTPException(status_code=404, detail='Temperature not found')
    return temperature


@app.delete('/temperature/{id}', tags=['Temperature'])
def delete_temperature(id: int, db: Session = Depends(get_db)):
    return TemperatureController.delete(db, id)


@app.post('/humidity/', response_model=Humidity, tags=['Humidity'])
def create_humidity(humidity: HumidityCreate, db: Session = Depends(get_db)):
    return HumidityController.create(db, humidity)


@app.get('/humidity/{id}', response_model=Humidity, tags=['Humidity'])
def get_humidity(id: int, db: Session = Depends(get_db)):
    humidity = HumidityController.get_one(db, id)
    if humidity is None:
        raise HTTPException(status_code=404, detail='Humidity not found')
    return humidity


@app.delete('/humidity/{id}', tags=['Humidity'])
def delete_humidity(id: int, db: Session = Depends(get_db)):
    return HumidityController.delete(db, id)


@app.post('/air-pressure/', response_model=AirPressure, tags=['Air Pressure'])
def create_air_pressure(air_pressure: AirPressureCreate, db: Session = Depends(get_db)):
    return AirPressureController.create(db, air_pressure)


@app.get('/air-pressure/{id}', response_model=AirPressure, tags=['Air Pressure'])
def get_air_pressure(id: int, db: Session = Depends(get_db)):
    air_pressure = AirPressureController.get_one(db, id)
    if air_pressure is None:
        raise HTTPException(status_code=404, detail='Air Pressure not found')
    return air_pressure


@app.delete('/air-pressure/{id}', tags=['Air Pressure'])
def delete_air_pressure(id: int, db: Session = Depends(get_db)):
    return AirPressureController.delete(db, id)
