import requests

BASE_URL = "http://localhost:8000"
ADMIN = {"username": "admin", "password": "adminpass"}
ESTUDIANTE = {"username": "estu", "password": "estupass"}

def get_token(user):
    resp = requests.post(f"{BASE_URL}/login", json=user)
    assert resp.status_code == 200
    return resp.json()["access_token"]

def test_asignacion_admin():
    token = get_token(ADMIN)
    headers = {"Authorization": f"Bearer {token}"}
    # Crear contenedor e imagen si es necesario
    # ...
    # Crear asignación
    resp = requests.post(f"{BASE_URL}/asignaciones", params={"usuario_id": 2, "contenedor_id": 1}, headers=headers)
    assert resp.status_code in [200, 400]  # Puede fallar si ya existe
    # Consultar asignaciones
    resp = requests.get(f"{BASE_URL}/asignaciones", params={"usuario_id": 2}, headers=headers)
    assert resp.status_code == 200
    # Borrar asignación
    if resp.json():
        asignacion_id = resp.json()[0]["id"]
        resp = requests.delete(f"{BASE_URL}/asignaciones/{asignacion_id}", headers=headers)
        assert resp.status_code == 200

def test_asignacion_estudiante_forbidden():
    token = get_token(ESTUDIANTE)
    headers = {"Authorization": f"Bearer {token}"}
    # Intentar crear asignación (debe fallar)
    resp = requests.post(f"{BASE_URL}/asignaciones", params={"usuario_id": 2, "contenedor_id": 1}, headers=headers)
    assert resp.status_code == 403 