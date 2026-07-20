from fastapi import FastAPI

from db import create_db_and_tables

app = FastAPI()
create_db_and_tables()

@app.get("/")
def main():
    return {"result": "Hello from Soundpost!"}



