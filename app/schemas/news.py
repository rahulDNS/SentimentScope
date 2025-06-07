from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NewsCreate(BaseModel):
    title: str
    content: str
    source: str
    country: str
    published_at: Optional[datetime] = None
    sentiment_score: Optional[float] = None
    sentiment_label: Optional[str] = None

class NewsResponse(NewsCreate):
    id: int

    class Config:
        orm_mode = True
