from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..hashing import verify_password
from .. import schemas, database, models, jwt_token

router = APIRouter(
  tags=['Authentication'])



@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
  user = db.query(models.User).filter(models.User.email==request.username).first()
  # user2 = db.query(models.User).filter(models.User.username==request.username).first()
  # user = user1 or user2
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')
  if not verify_password(request.password, user.password):
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect password')

  access_token = jwt_token.create_access_token(data={"sub": user.email})
  return {"access_token": access_token, "token_type": "bearer"}
  
