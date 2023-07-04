from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..hashing import hash_password
from ..repository import user, definition

router = APIRouter(
  prefix='/user',
  tags=['User']
)



@router.post('', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
  # hashedPassword = pwd_context.hash(request.password)
  # return user.create_user(request, db)
  user = models.User(username=request.username, email=request.email, password=hash_password(request.password)) # type: ignore
  return definition.create_query(user, request, db)

@router.get('', response_model=list[schemas.ShowUser])
def show_users(db: Session = Depends(database.get_db)):
  # return user.get_all_users(db)
  return definition.get_all(models.User, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def user_detail(id: int, db: Session = Depends(database.get_db)):
  # return user.get_user_detail(id, db)
  return definition.get_detail(models.User, id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(database.get_db)):
  # return blog.delete_blog(id, db)  
  return definition.delete_query(models.User, id, db)
