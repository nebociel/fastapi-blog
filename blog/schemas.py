from pydantic import BaseModel


class BlogBase(BaseModel):
  title: str
  body: str

class Blog(BlogBase):
  user_id: int
  
  class Config():
    orm_mode = True
          

class User(BaseModel):
  username: str
  email: str
  password: str

class ShowUser(BaseModel):
  username: str
  email: str
  blogs: list[Blog]

  class Config():
    orm_mode = True


class ShowBlog(BaseModel):
  id: int
  title: str
  body: str
  author: ShowUser
  
  class Config():
    orm_mode = True


class Login(BaseModel):
  username: str
  password: str


# jwt token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None