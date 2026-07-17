from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__ = "users" # type: ignore
    id: int = Field(primary_key=True)
    username: str
    email: str
    password_hash: str
    created_at: str

class Artist(SQLModel, table=True):
    __tablename__ = "artists" # type: ignore
    pass

class Album(SQLModel, table=True):
    __tablename__ = "albums" # type: ignore
    pass

class Track(SQLModel, table=True):
    __tablename__ = "tracks" # type: ignore
    pass

class Scrobble(SQLModel, table=True):
    __tablename__ = "scrobbles" # type: ignore
    pass