#This function ensures that items can be removed or their quantities 
#reduced in a cart efficiently and handles cases where the item is not found appropriately.

from sqlmodel import Session, select
from app.models import Cart, ItemsInCart, Item
from fastapi import HTTPException

def create_cart(session: Session) -> Cart:
    cart = Cart()
    session.add(cart)
    session.commit()
    session.refresh(cart)
    return cart

def get_cart(session: Session, cart_id: int) -> Cart:
    return session.get(Cart, cart_id)

def delete_cart(session: Session, cart_id: int) -> None:
    cart = get_cart(session, cart_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    session.delete(cart)
    session.commit()

def add_item_to_cart(session: Session, cart_id: int, item_id: int, quantity: int) -> ItemsInCart:
    cart = get_cart(session, cart_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    cart_item = session.exec(
        select(ItemsInCart).where(ItemsInCart.cart_id == cart_id, ItemsInCart.item_id == item_id)
    ).one_or_none()

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = ItemsInCart(cart_id=cart_id, item_id=item_id, quantity=quantity)
        session.add(cart_item)
    
    session.commit()
    session.refresh(cart_item)
    return cart_item
