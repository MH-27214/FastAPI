from fastapi import FastAPI
from db.database import engine
from db import models
from router import user
app = FastAPI()

app.include_router(user.router)

@app.get("/hello")
async def index():
    return {"message": "Hello World"}

models.Base.metadata.create_all(engine)
#DDDD
