from fastapi import FastAPI
from app.database.session import engine
from app.database import models

# ✅ This will auto-create tables in the MySQL database if they don’t exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to SentimentScope API"}


