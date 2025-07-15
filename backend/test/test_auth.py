import requests

BASE_URL = "http://localhost:8000"


def test_register():
    data = {"username": "testuser", "password": "testpass"}
    response = requests.post(f"{BASE_URL}/register", json=data)
    assert response.status_code in [200, 400]  # 400 si el usuario ya existe
    if response.status_code == 200:
        assert response.json()["username"] == data["username"]


def test_login_success():
    data = {"username": "testuser", "password": "testpass"}
    response = requests.post(f"{BASE_URL}/login", json=data)
    assert response.status_code == 200
    json_data = response.json()
    assert "access_token" in json_data
    assert json_data["token_type"] == "bearer"
    return json_data["access_token"]


def test_login_fail():
    data = {"username": "testuser", "password": "wrongpass"}
    response = requests.post(f"{BASE_URL}/login", json=data)
    assert response.status_code == 401


def test_me():
    token = test_login_success()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/me", headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["username"] == "testuser"

if __name__ == "__main__":
    test_register()
    test_login_success()
    test_login_fail()
    test_me() 