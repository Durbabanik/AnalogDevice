from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.models import Item
from app.dependencies import get_session

router = APIRouter(prefix="/items")

@router.post("/", response_model=Item)
def create_item(item: Item, session: Session = Depends(get_session)):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@router.delete("/{item_id}")
def delete_item(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Item, item_id)
    if item:
        session.delete(item)
        session.commit()
    return {"detail": "Item deleted"}

