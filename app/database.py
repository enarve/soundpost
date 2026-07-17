from sqlmodel import create_engine
from sqlmodel.main import SQLModel

engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)

