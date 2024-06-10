#Entry point for the FastAPI application. This file initializes the FastAPI app, 
#includes routers, and sets up metrics and health check endpoints.

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.routers import carts, items

app = FastAPI()

app.include_router(carts.router)
app.include_router(items.router)

# Add Prometheus Instrumentator
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}

