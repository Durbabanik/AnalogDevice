#This allows to model a typical shopping cart system where each cart can contain multiple items, and each item can appear in multiple carts, 
#with quantities tracked for each item in each cart.

from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    carts: List["ItemsInCart"] = Relationship(back_populates="item")

class Cart(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    items: List["ItemsInCart"] = Relationship(back_populates="cart")

class ItemsInCart(SQLModel, table=True):
    cart_id: Optional[int] = Field(default=None, foreign_key="cart.id", primary_key=True)
    item_id: Optional[int] = Field(default=None, foreign_key="item.id", primary_key=True)
    quantity: int = Field(default=1)
    cart: Optional[Cart] = Relationship(back_populates="items")
    item: Optional[Item] = Relationship(back_populates="carts")

