import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from login_db.models import Base


# Create an engine
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
engine = create_engine(f"postgresql+psycopg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)