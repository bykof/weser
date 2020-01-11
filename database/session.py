from sqlalchemy.orm import sessionmaker

from database.engine import engine

LocalSession = sessionmaker(bind=engine)
