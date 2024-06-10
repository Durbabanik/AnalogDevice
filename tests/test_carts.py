#contains a series of test cases implemented using the pytest 
#framework to test the functionality of an API for managing shopping carts.
import pytest
from sqlmodel import Session
from app.models import Cart, Item, ItemsInCart
from app.crud import create_cart, delete_cart, get_cart, add_item_to_cart, remove_item_from_cart

# Test case: Create a cart – Does create the shopping cart
def test_create_cart(client):
    response = client.post("/carts/")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data

# Test case: Delete a cart – Does delete the shopping cart
def test_delete_cart(client):
    response = client.post("/carts/")
    cart_id = response.json()["id"]
    response = client.delete(f"/carts/{cart_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Cart deleted"}

# Test case: Delete a non-existent cart – Raises an error
def test_delete_nonexistent_cart(client):
    response = client.delete("/carts/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Cart not found"}

# Test case: Remove an item from a cart – lowers the count of that item by 1, with a minimum being 0
def test_remove_item_from_cart(client):
    # Create a cart and an item
    cart_response = client.post("/carts/")
    cart_id = cart_response.json()["id"]
    item_response = client.post("/items/", json={"name": "item1", "price": 10.0})
    item_id = item_response.json()["id"]

    # Add item to the cart
    client.post(f"/carts/{cart_id}/items/{item_id}", json={"quantity": 5})

    # Remove item from the cart
    client.post(f"/carts/{cart_id}/items/{item_id}/remove", json={"quantity": 1})
    response = client.get(f"/carts/{cart_id}")
    cart_data = response.json()
    assert any(item["id"] == item_id and item["quantity"] == 4 for item in cart_data["items"])

# Test case: Remove a non-existent item from a cart – Raises an error
def test_remove_nonexistent_item_from_cart(client):
    cart_response = client.post("/carts/")
    cart_id = cart_response.json()["id"]
    response = client.post(f"/carts/{cart_id}/items/9999/remove", json={"quantity": 1})
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found in cart"}

