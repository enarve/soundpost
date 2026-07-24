from sqlmodel import create_engine
from sqlmodel.main import SQLModel

from . import models

database_url = "sqlite:///database.db"
engine = create_engine(database_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)