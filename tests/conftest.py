#pytest setup code is designed for testing FastAPI applications that use SQLModel for interacting with a database.
import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from app.main import app
from app.dependencies import get_session

# Set up the test database URL (use an in-memory SQLite database for simplicity)
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Dependency override to use the test database
def override_get_session():
    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture():
    app.dependency_overrides[get_session] = override_get_session
    with TestClient(app) as client:
        yield client

@pytest.fixture(autouse=True)
def setup_and_teardown():
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)

