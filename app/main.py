from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from app import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your allowed origins here
    allow_credentials=True,
    allow_methods=["*"],  # Or specify the methods you want to allow
    allow_headers=["*"],  # Or specify the headers you want to allow
)

@app.post("/hustles/", response_model=schemas.Hustle)
def create_hustle(hustle: schemas.HustleCreate, db: Session = Depends(database.get_db)):
    return crud.create_hustle(db, hustle)

@app.get("/hustles/{hustle_id}", response_model=schemas.Hustle)
def read_hustle(hustle_id: int, db: Session = Depends(database.get_db)):
    db_hustle = crud.get_hustle(db, hustle_id)
    if db_hustle is None:
        raise HTTPException(status_code=404, detail="Hustle not found")
    return db_hustle

@app.get("/hustles/", response_model=list[schemas.Hustle])
def read_hustles(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_hustles(db, skip, limit)

@app.put("/hustles/{hustle_id}", response_model=schemas.Hustle)
def update_hustle(hustle_id: int, hustle: schemas.HustleCreate, db: Session = Depends(database.get_db)):
    return crud.update_hustle(db, hustle_id, hustle)

@app.delete("/hustles/{hustle_id}", response_model=schemas.Hustle)
def delete_hustle(hustle_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_hustle(db, hustle_id)
