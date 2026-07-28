from fastapi import FastAPI
from sqlmodel import Session, select

from models import Artist
from db import create_db_and_tables, create_test_data, engine

app = FastAPI()
create_db_and_tables()
create_test_data()

@app.get("/")
def main():
    return {"result": "Hello from Soundpost!"}

@app.get("/artists")
def artists():
    with Session(engine) as session:
        statement = select(Artist)
        results = session.exec(statement)
        artists = results.all()
        return {"result": artists}

@app.get("/add_artist")
def add_artist():
    new_artist = Artist(name="Test Artist")
    print(new_artist.id)
    with Session(engine) as session:
        session.add(new_artist)
        print(new_artist.id)
        session.commit()
        session.refresh(new_artist)
    print(new_artist.id)
