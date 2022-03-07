from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from basic_auth import schemas, database, oauth2
from sqlalchemy.orm import Session
from basic_auth.repository import item

router = APIRouter(
    prefix="/item",
    tags=['Items']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowItem])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Item, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Item, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowItem)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return item.show(id, db)
