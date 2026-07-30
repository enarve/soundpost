from sqlmodel import SQLModel, Session, create_engine

from app.models import Artist

database_url = "sqlite:///database.db"
engine = create_engine(database_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_test_data():
    artist_1 = Artist(name="A Hawk and a Hacksaw")
    artist_2 = Artist(name="Johann Sebastian Bach")

    with Session(engine) as session:
        session.add(artist_1)
        session.add(artist_2)
        
        session.commit()