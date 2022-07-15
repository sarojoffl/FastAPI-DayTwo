from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import database
import models


app = FastAPI()


@app.get("/student/{id}")
def get_user(id: int, db: Session = Depends(database.get_db)):
    data = db.query(models.UserTBL).filter(models.UserTBL.user_id == id).first()
    return {"data": data}
