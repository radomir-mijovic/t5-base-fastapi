from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_should_redirect_user_to_docs() -> None:
    response = client.get("/")
    assert response.request.url == "http://testserver/docs"
    assert "Swagger" in response.text
