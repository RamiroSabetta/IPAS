import requests

BASE_URL = "http://localhost:8000"

# Utilidades para autenticación
ADMIN = {"username": "admin", "password": "adminpass"}
ESTUDIANTE = {"username": "estu", "password": "estupass"}

def get_token(user):
    resp = requests.post(f"{BASE_URL}/login", json=user)
    assert resp.status_code == 200
    return resp.json()["access_token"]

def test_crud_contenedor_admin():
    token = get_token(ADMIN)
    headers = {"Authorization": f"Bearer {token}"}
    # Crear contenedor
    data = {
        "nombre": "Cont1",
        "descripcion": "desc",
        "imagen": 1,  # Debe existir una imagen con id=1
        "estado": "activo",
        "puertos": {"8080": "80"}
    }
    resp = requests.post(f"{BASE_URL}/contenedores", json=data, headers=headers)
    assert resp.status_code == 200
    cont = resp.json()
    cont_id = cont["id"]
    # Obtener contenedor
    resp = requests.get(f"{BASE_URL}/contenedores/{cont_id}", headers=headers)
    assert resp.status_code == 200
    # Actualizar contenedor
    data["estado"] = "inactivo"
    resp = requests.put(f"{BASE_URL}/contenedores/{cont_id}", json=data, headers=headers)
    assert resp.status_code == 200
    # Eliminar contenedor
    resp = requests.delete(f"{BASE_URL}/contenedores/{cont_id}", headers=headers)
    assert resp.status_code == 200

def test_contenedor_estudiante_asignado():
    # Asignar contenedor al estudiante (como admin)
    admin_token = get_token(ADMIN)
    headers_admin = {"Authorization": f"Bearer {admin_token}"}
    # Crear contenedor
    data = {
        "nombre": "Cont2",
        "descripcion": "desc2",
        "imagen": 1,
        "estado": "activo",
        "puertos": {"8081": "81"}
    }
    resp = requests.post(f"{BASE_URL}/contenedores", json=data, headers=headers_admin)
    assert resp.status_code == 200
    cont_id = resp.json()["id"]
    # Asignar
    resp = requests.post(f"{BASE_URL}/asignaciones", params={"usuario_id": 2, "contenedor_id": cont_id}, headers=headers_admin)
    assert resp.status_code == 200
    # Login estudiante
    token = get_token(ESTUDIANTE)
    headers = {"Authorization": f"Bearer {token}"}
    # Listar contenedores asignados
    resp = requests.get(f"{BASE_URL}/contenedores", headers=headers)
    assert resp.status_code == 200
    assert any(c["id"] == cont_id for c in resp.json())
    # Eliminar asignación (como admin)
    asignacion_id = resp.json()[0]["id"]
    resp = requests.delete(f"{BASE_URL}/asignaciones/{asignacion_id}", headers=headers_admin)
    assert resp.status_code == 200
    # Eliminar contenedor
    resp = requests.delete(f"{BASE_URL}/contenedores/{cont_id}", headers=headers_admin)
    assert resp.status_code == 200

def test_asignaciones_por_usuario():
    token = get_token(ADMIN)
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"{BASE_URL}/asignaciones", params={"usuario_id": 2}, headers=headers)
    assert resp.status_code == 200 