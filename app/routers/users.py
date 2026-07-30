from fastapi import APIRouter
from sqlmodel import Session

from app.models import User
from app.db import engine

router = APIRouter()

@router.get("/")
def main():
    return {"users": "me"}

@router.post("/create")
def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()