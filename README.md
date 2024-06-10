# AnalogDevice
assignment

# FastAPI Shopping Cart Application

**Introduction**
This is a simple shopping cart application built using FastAPI and SQLModel. The application supports adding items to carts, viewing cart contents, and removing items from carts.

**Features**
Create and delete shopping carts.
Add items to a cart.
Remove items from a cart.
View cart contents.
Health check endpoint.
Metrics endpoint for Prometheus.

# Setup and Installation

- Clone the repository:
- Create a virtual environment and activate it
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Running the Application

- docker-compose up --build
- Open your browser and navigate to http://0.0.0.0:8000.
- Access the API documentation at http://0.0.0.0:8000/docs. (swagger UI)

![image](https://github.com/bcg-cpe-shared-tooling/bcg-cpe-terraform-aws-ipam/assets/108435425/31114976-0e75-4a0c-9bc7-29a68ecf145e)

# The docker compose file 

The docker-compose.yml file sets up a multi-container environment with two main services:

web: The FastAPI application container, which is built from the local Dockerfile and runs the application on port 8000. It connects to the PostgreSQL database using an environment variable for the database URL.
db: The PostgreSQL database container, which uses the official PostgreSQL 13 image and sets up a database with a specified user, password, and database name. It also persists data using a named volume.

# API Endpoints

Carts
POST /carts/

Create a new cart.
GET /carts/{cart_id}

Get a specific cart by ID.
DELETE /carts/{cart_id}

Delete a specific cart by ID.
Items
POST /items/

Create a new item.
GET /items/{item_id}

Get a specific item by ID.
Items in Cart
POST /carts/{cart_id}/items/{item_id}

Add an item to a cart.
POST /carts/{cart_id}/items/{item_id}/remove

Remove an item from a cart.





