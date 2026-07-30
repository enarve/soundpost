from fastapi import FastAPI
from sqlmodel import Session, select, col

from app.models import Artist
from app.db import create_db_and_tables, create_test_data, engine
from app.routers import users

app = FastAPI()
app.include_router(users.router, prefix="/api/users", tags=["users"])

create_db_and_tables()
create_test_data()

@app.get("/")
def main():
    return {"result": "Hello from Soundpost!"}

@app.get("/artists")
def artists():
    with Session(engine) as session:
        statement = select(Artist).where(col(Artist.id) > 1)
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
