from sqlalchemy.orm import Session
from app import models, schemas

def create_hustle(db: Session, hustle: schemas.HustleCreate):
    db_hustle = models.Hustle(**hustle.dict())
    db.add(db_hustle)
    db.commit()
    db.refresh(db_hustle)
    return db_hustle

def get_hustle(db: Session, hustle_id: int):
    return db.query(models.Hustle).filter(models.Hustle.id == hustle_id).first()

def get_hustles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Hustle).offset(skip).limit(limit).all()

def update_hustle(db: Session, hustle_id: int, hustle: schemas.HustleCreate):
    db_hustle = get_hustle(db, hustle_id)
    if db_hustle:
        for key, value in hustle.dict().items():
            setattr(db_hustle, key, value)
        db.commit()
        db.refresh(db_hustle)
    return db_hustle

def delete_hustle(db: Session, hustle_id: int):
    db_hustle = get_hustle(db, hustle_id)
    if db_hustle:
        db.delete(db_hustle)
        db.commit()
    return db_hustle
