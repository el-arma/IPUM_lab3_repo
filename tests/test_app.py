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


def test_my_flower():
    # Iris setosa
    X_new = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }

    response = r.post(f"{url}/predict", json=X_new)

    assert response.status_code == 200

    assert response.json() == {"prediction": "Iris setosa"}
