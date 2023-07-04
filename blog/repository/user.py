from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from ..hashing import hash_password
from .. import models


def get_all_users(db: Session):
  users = db.query(models.User).all()
  return users

def get_user_detail(id: int, db: Session):
  user = db.query(models.User).filter(models.User.id==id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
  return user

def create_user(request, db):
  user = models.User(username=request.username, email=request.email, password=hash_password(request.password))
  db.add(user)
  db.commit()
  db.refresh(user)
  return user