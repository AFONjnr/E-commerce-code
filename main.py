from fastapi import FastAPI
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise
from models import *


app=FastAPI()

@app.get("/")
def index():
    return{"message": "hello world"}



register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models" : ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)