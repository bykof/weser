import os

from sqlalchemy import create_engine


engine = create_engine(
    os.environ.get('DB_URL', 'sqlite:///./db.sqlite'),
    connect_args={"check_same_thread": False}
)
