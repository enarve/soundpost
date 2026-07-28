from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: int | None = Field(default=None, primary_key=True)
    created_at: str | None
    username: str
    email: str
    password_hash: str
    
    display_name: str | None = None
    about: str | None = None
    website: str | None = None

class Artist(SQLModel, table=True):
    __tablename__ = "artists"

    id: int | None = Field(default=None, primary_key=True)
    created_at: str | None = None
    name: str
    
    about: str | None = None
    

# class Album(SQLModel, table=True):
#     __tablename__ = "albums"
#     pass

# class Track(SQLModel, table=True):
#     __tablename__ = "tracks"
#     pass

# class Scrobble(SQLModel, table=True):
#     __tablename__ = "scrobbles"
#     pass