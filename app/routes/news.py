from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.news import NewsCreate, NewsResponse
from app.database.models import News
from app.database.session import SessionLocal
from typing import List

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /news → store a news article
@router.post("/news", response_model=NewsResponse)
def create_news(news: NewsCreate, db: Session = Depends(get_db)):
    db_news = News(**news.dict())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

# GET /news → return all news articles
@router.get("/news", response_model=List[NewsResponse])
def get_all_news(db: Session = Depends(get_db)):
    return db.query(News).order_by(News.published_at.desc()).all()
