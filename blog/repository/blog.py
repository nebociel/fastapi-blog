from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import models


def get_all_blogs(db: Session):
  blogs = db.query(models.Blog).all()
  return blogs

def get_blog_detail(id: int, db: Session):
  blog = db.query(models.Blog).filter(models.Blog.id==id).first()
  if not blog:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} does not exist')
  return blog

def create_blog(request, db):
  new_blog = models.Blog(title=request.title, body=request.body, user_id=request.user_id)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog

def delete_blog(id, db):
  blog = db.query(models.Blog).filter(models.Blog.id==id)
  if not blog.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
  blog.delete(synchronize_session=False)
  db.commit()
  return 'Deleted'

def update_blog(id, request, db):
  blog = db.query(models.Blog).filter(models.Blog.id==id)
  if not blog.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
  blog.update(request.dict())
  db.commit()
  return 'Updated'