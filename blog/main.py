from fastapi import FastAPI
from .database import engine
from .routers import user, blog, authentication
from . import models

# from fastapi import FastAPI, Depends, Response, status, HTTPException
# from sqlalchemy.orm import Session
# from random import randrange
# from .hashing import hash_password
# from passlib.context import CryptContext
# from .database import SessionLocal, engine
# from .routers import user, blog
# from . import schemas, models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(blog.router)
app.include_router(authentication.router)

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blog'])
# def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
#   new_blog = models.Blog(title=request.title, body=request.body, user_id=randrange(5))
#   db.add(new_blog)
#   db.commit()
#   db.refresh(new_blog)
#   return new_blog

# @app.get('/blog', response_model=list[schemas.ShowBlog], tags=['blog'])
# def show_blogs(db: Session = Depends(get_db)):
#   blogs = db.query(models.Blog).all()
#   return blogs

# @app.get('/blog/{id}', response_model=schemas.ShowBlog, tags=['blog'])
# def blog_detail(id: int, response: Response, db: Session = Depends(get_db)):
#   blog = db.query(models.Blog).filter(models.Blog.id==id).first()
#   if not blog:
#     # response.status_code = status.HTTP_404_NOT_FOUND
#     # return {'detail' : f'Blog with id {id} does not exist'}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} does not exist')
#   return blog

# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blog'])
# def destroy_blog(id: int, db: Session = Depends(get_db)):
#   blog = db.query(models.Blog).filter(models.Blog.id==id)
#   if not blog.first():
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
#   blog.delete(synchronize_session=False)
#   db.commit()
#   return 'Deleted'

# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blog'])
# def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
#   blog = db.query(models.Blog).filter(models.Blog.id==id)
#   if not blog.first():
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
#   blog.update(request.dict())
#   db.commit()
#   return 'Updated'



# @app.get('/users', response_model=list[schemas.ShowUser], tags=['user'])
# def show_users(db: Session = Depends(get_db)):
#   users = db.query(models.User).all()
#   return users

# @app.post('/user', response_model=schemas.ShowUser, tags=['user'])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#   # hashedPassword = pwd_context.hash(request.password)
#   user = models.User(username=request.username, email=request.email, password=hash_password(request.password))
#   db.add(user)
#   db.commit()
#   db.refresh(user)
#   return user

# @app.get('/users/{id}', response_model=schemas.ShowUser, tags=['user'])
# def user_detail(id: int, db: Session = Depends(get_db)):
#   user = db.query(models.User).filter(models.User.id==id).first()
#   if not user:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
#   return user