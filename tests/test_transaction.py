from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.db.database import get_db

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_transaction():
    response = client.post('/transactions/', json={'amount': 100.0, 'description': 'Test transaction'})
    assert response.status_code == 200
    assert response.json()['amount'] == 100.0

def test_read_transaction():
    response = client.get('/transactions/1')
    assert response.status_code == 200
    assert response.json()['id'] == 1

def test_update_transaction():
    response = client.put('/transactions/1', json={'amount': 200.0, 'description': 'Updated transaction'})
    assert response.status_code == 200
    assert response.json()['amount'] == 200.0

def test_delete_transaction():
    response = client.delete('/transactions/1')
    assert response.status_code == 200
    assert response.json()['id'] == 1