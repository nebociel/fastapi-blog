from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
  # return {"data": "blog list"}
  if published:
    return {'data' : f'{limit} published blogs returned'}
  else:
    return {'data' : f'{limit} blogs returned'}


@app.get('/blog/unpublished')
def unpublished():
  return {"data": "all unpublished blogs"}


@app.get('/blog/{id}')
def about(id: int):
  return {"data": id}


@app.get('/blog/{id}/comments')
def comments(id: int):
  return {"data": {'1', '2'}}



class Blog(BaseModel):
  title: str
  body: str
  published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
  # return request
  return {f'{request.title}, {request.body}, {request.published}'}