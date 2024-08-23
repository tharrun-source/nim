from pydantic import BaseModel
from datetime import datetime

class HustleBase(BaseModel):
    name: str
    description: str
    income: float
    expenses: float
    date: datetime

class HustleCreate(HustleBase):
    pass

class Hustle(HustleBase):
    id: int

    class Config:
        orm_mode = True
