from sqlmodel import create_engine
from sqlmodel.main import SQLModel
import models

database_filename = "database.db"
database_url = f"sqlite:///{database_filename}"
engine = create_engine(database_url, echo=True)



