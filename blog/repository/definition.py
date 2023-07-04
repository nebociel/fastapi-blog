from fastapi import status, HTTPException
from sqlalchemy.orm import Session


def get_all(model, db: Session):
  query = db.query(model).all()
  return query

def get_detail(model, id: int, db: Session):
  query = db.query(model).filter(model.id==id).first()
  if not query:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'query with id {id} does not exist')
  return query

def create_query(new_query, request, db: Session):
  new_query = new_query
  db.add(new_query)
  db.commit()
  db.refresh(new_query)
  return new_query

def delete_query(model, id: int, db: Session):
  query = db.query(model).filter(model.id==id)
  if not query.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'query with id {id} not found')
  query.delete(synchronize_session=False)
  db.commit()
  return 'Deleted'

def update_query(model, id: int, request, db):
  query = db.query(model).filter(model.id==id)
  if not query.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'query with id {id} not found')
  query.update(request.dict())
  db.commit()
  return 'Updated'