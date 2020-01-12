import os

from sqlalchemy import create_engine

DB_URL = os.environ.get('DB_URL', 'sqlite:///./db.sqlite')
engine = create_engine(
    DB_URL,
    connect_args={"check_same_thread": 'sqlite' in DB_URL}
)
