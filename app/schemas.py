#These Pydantic models are used to validate input data, ensure type safety, and facilitate easy serialization 
#and deserialization of data when working with APIs and databases.

from typing import List, Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode: True

class CartBase(BaseModel):
    pass

class CartCreate(CartBase):
    pass

class Cart(CartBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode: True

class ItemsInCartBase(BaseModel):
    cart_id: int
    item_id: int
    quantity: int

class ItemsInCartCreate(ItemsInCartBase):
    pass

class ItemsInCart(ItemsInCartBase):
    pass

