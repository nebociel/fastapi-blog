from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Blog(Base):
  __tablename__ = "blogs"
  
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  body = Column(String)
  user_id = Column(Integer, ForeignKey('users.id'))

  author = relationship("User", back_populates="blogs")

class User(Base):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  email = Column(String, unique=True)
  password = Column(String)

  blogs = relationship("Blog", back_populates="author")