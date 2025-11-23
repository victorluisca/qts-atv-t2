from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_item_success():
    response = client.get("/items/1")
    assert response.status_code == 200


def test_get_item_fail():
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
