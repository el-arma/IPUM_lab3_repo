import requests as r

PORT = 8000

url = f"http://localhost:{PORT}"


def test_root_route():
    response = r.get(url)
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_route():
    response = r.get(f"{url}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
