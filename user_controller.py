
from fastapi import APIRouter, Depends, Response, Request
from sqlalchemy.orm import Session
from typing import Dict

from schemas import User, UserUpdate

from database import SessionLocal, engine, get_db
import models


user_router_v1 = APIRouter(prefix='/api/v1/users')

@user_router_v1.get("/")
async def get_user(db: Session = Depends(get_db)):
    """Get all users."""
    try:
        return db.query(models.User).all()
    except:
        return { "message" : "Unable to retrieve users. Please try again later."}

@user_router_v1.get("/{s_id}")
async def get_specific_user(s_id: int, response: Response, db: Session = Depends(get_db)):
    """Get a specific user."""
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
async def create_user(user: User, response: Response, db: Session = Depends(get_db)):
    """Create a new user."""
    try:
        if db.query(models.User).filter(models.User.sid == user.sid).first() is not None:
            response.status_code = 400
            return { "message" : "Unable to create user. User SID already exist."}
        user = models.User(sid=user.sid, first_name=user.first_name, last_name=user.last_name, dob=user.dob, sex=user.sex, bio=user.bio)
        db.add(user)
        db.commit()
        return { "message" : "User created successfully"}
    except Exception as e:
        response.status_code = 500
        return { "message" : "Unable to create user. Please try again later."}
    
@user_router_v1.patch('/{s_id}')
async def update_user(s_id: str, user: UserUpdate, db: Session = Depends(get_db)) -> Dict:
    """Update a user."""
    db_user = db.query(models.User).filter(models.User.sid == s_id).first()
    if not db_user:
        Response.status_code = 404
        return {"message": "Unable to update user. User not found."}
    update_data = user.model_dump(exclude_unset=True) 
    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return {"message": "User updated successfully"}


@user_router_v1.patch('/{s_id}')
async def delete_user(s_id: str, db: Session = Depends(get_db)) -> Dict:
    """Update a user."""
    db_user = db.query(models.User).filter(models.User.sid == s_id).first()
    if not db_user:
        Response.status_code = 404
        return {"message": "Unable to delete user. User not found."}
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}