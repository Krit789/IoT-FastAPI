
from fastapi import APIRouter, Depends, Response, Request
from sqlalchemy.orm import Session

from database import SessionLocal, engine, get_db
import models

user_router_v1 = APIRouter(prefix='/api/v1/users')

@user_router_v1.get("/")
async def get_user(db: Session = Depends(get_db)):
    try:
        return db.query(models.User).all()
    except:
        return { "message" : "Unable to retrieve users. Please try again later."}

@user_router_v1.get("/{s_id}")
async def get_specific_user(s_id: int, response: Response, db: Session = Depends(get_db)):
    try:
        user = db.query(models.User).filter(models.User.sid == s_id).first()
        if (user is None):
            response.status_code = 404
            return { "message" : f"User {s_id} not found" }
        return user
    except:
        response.status_code = 500
        return { "message" : "Unable to retrieve user. Please try again later."}

@user_router_v1.put('/')
async def create_user(user: dict, response: Response, db: Session = Depends(get_db)):
    try:
        user = models.User(first_name=user['first_name'])
        db.add(user)
        db.commit()
        return { "message" : "User created successfully"}
    except:
        response.status_code = 500
        return { "message" : "Unable to retrieve user. Please try again later."}
