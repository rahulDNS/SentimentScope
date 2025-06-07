from fastapi import FastAPI
from app.database.session import engine
from app.database import models
from app.routes import news  # 👈 new import

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(news.router)  # 👈 new line

@app.get("/")
async def read_root():
    return {"message": "Welcome to SentimentScope API"}
