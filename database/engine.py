import os

from sqlalchemy import create_engine

DB_URL = os.environ.get('DB_URL', 'sqlite:///./db.sqlite')
connection_args = {}

if 'sqlite' in DB_URL:
    connection_args['check_same_thread'] = True

engine = create_engine(
    DB_URL,
    connect_args=connection_args,
)
