import pytest
from tortoise.contrib.test import initializer, finalizer
from models.usuario import Usuario
from models.imagen import Imagen
from models.contenedor import Contenedor
from models.asignacion import Asignacion

@pytest.fixture(scope="module", autouse=True)
def setup():
    initializer(["models.usuario", "models.imagen", "models.contenedor", "models.asignacion"], db_url="sqlite://:memory:")
    yield
    finalizer()

def test_usuario():
    user = Usuario(username="test", password="123", perfil="admin")
    assert user.username == "test"

def test_imagen():
    img = Imagen(nombre="img1")
    assert img.nombre == "img1"

def test_contenedor():
    img = Imagen(nombre="img2")
    c = Contenedor(nombre="c1", imagen=img)
    assert c.nombre == "c1"

def test_asignacion():
    user = Usuario(username="test2", password="123", perfil="estudiante")
    img = Imagen(nombre="img3")
    c = Contenedor(nombre="c2", imagen=img)
    a = Asignacion(usuario=user, contenedor=c)
    assert a.usuario.username == "test2" 