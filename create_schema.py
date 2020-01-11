from database.engine import engine
from models.base import Base

Base.metadata.create_all(engine)
