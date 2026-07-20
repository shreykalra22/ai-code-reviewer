from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from app.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    language = Column(String, nullable=False)
    code = Column(Text, nullable=False)
    review = Column(Text, nullable=False)
    improved_code = Column(Text, nullable=True)
    score = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)