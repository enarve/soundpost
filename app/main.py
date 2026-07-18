from fastapi import FastAPI

from db import SQLModel, engine

app = FastAPI()
SQLModel.metadata.create_all(engine)

@app.get("/")
def main():
    return {"result": "Hello from Soundpost!"}



