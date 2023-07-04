from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..repository import blog, definition
from .. import schemas, database, models, oauth2

router = APIRouter(
  prefix='/blog',
  tags=['Blog']
)



@router.post('', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
  # return blog.create_blog(request, db)
  new_query = models.Blog(title=request.title, body=request.body, user_id=request.user_id)
  if not db.query(models.User).filter(models.User.id==new_query.user_id).first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {new_query.user_id} does not exist')
  return definition.create_query(new_query, request, db)


@router.get('', response_model=list[schemas.ShowBlog])
def show_blogs(db: Session = Depends(database.get_db)):
  # return blog.get_all_blogs(db)
  return definition.get_all(models.Blog, db)  


@router.get('/{id}', response_model=schemas.ShowBlog)
def blog_detail(id: int, db: Session = Depends(database.get_db)):
  # return blog.get_blog_detail(id, db)
  return definition.get_detail(models.Blog, id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
  # return blog.delete_blog(id, db)  
  return definition.delete_query(models.Blog, id, db)
  

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
  # return blog.update_blog(id, request, db)
  return definition.update_query(models.Blog, id, request, db)
