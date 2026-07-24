from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: str
    password_hash: str
    created_at: str
    
    display_name: str | None = None
    about_me: str | None = None
    website: str | None = None

# class Artist(SQLModel, table=True):
#     __tablename__ = "artists"
#     pass

# class Album(SQLModel, table=True):
#     __tablename__ = "albums"
#     pass

# class Track(SQLModel, table=True):
#     __tablename__ = "tracks"
#     pass

# class Scrobble(SQLModel, table=True):
#     __tablename__ = "scrobbles"
#     pass