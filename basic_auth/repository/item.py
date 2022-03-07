from sqlalchemy.orm import Session
from basic_auth import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    items = db.query(models.Item).all()
    return items


def create(request: schemas.Item, db: Session):
    new_item = models.Item(title=request.title, body=request.body, user_id=1)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def destroy(id: int, db: Session):
    item = db.query(models.Item).filter(models.Item.id == id)

    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    item.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Item, db: Session):
    item = db.query(models.Item).filter(models.Item.id == id)

    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    item.update(request)
    db.commit()
    return 'updated'


def show(id: int, db: Session):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not available")
    return item
