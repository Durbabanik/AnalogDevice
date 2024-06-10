from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.models import Cart, ItemsInCart
from app.crud import create_cart, get_cart, delete_cart, add_item_to_cart
from app.dependencies import get_session

router = APIRouter(prefix="/carts")

@router.post("/", response_model=Cart)
def create_new_cart(session: Session = Depends(get_session)):
    return create_cart(session)

@router.get("/{cart_id}", response_model=Cart)
def read_cart(cart_id: int, session: Session = Depends(get_session)):
    cart = get_cart(session, cart_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return cart

@router.delete("/{cart_id}")
def remove_cart(cart_id: int, session: Session = Depends(get_session)):
    delete_cart(session, cart_id)
    return {"detail": "Cart deleted"}

@router.post("/{cart_id}/items/{item_id}")
def add_item(cart_id: int, item_id: int, quantity: int, session: Session = Depends(get_session)):
    add_item_to_cart(session, cart_id, item_id, quantity)
    return {"detail": "Item added"}
