from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime
from .session import Base

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    content = Column(String(5000))  # ✅ Added length
    source = Column(String(100))
    country = Column(String(50))
    published_at = Column(DateTime, default=datetime.utcnow)
    sentiment_score = Column(Float)
    sentiment_label = Column(String(20))

class Trend(Base):
    __tablename__ = "trends"
    id = Column(Integer, primary_key=True, index=True)
    sector = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)
    trend_prediction = Column(String(20))  # Bullish/Bearish
