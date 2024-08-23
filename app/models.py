from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Hustle(Base):
    __tablename__ = "hustles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    income = Column(Float, default=0.0)
    expenses = Column(Float, default=0.0)
    date = Column(DateTime)
