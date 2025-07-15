# Pruebas Unitarias del Backend

Este directorio contiene las pruebas unitarias para los servicios y modelos del backend de IPAS.

## Requisitos

- Python 3.9+
- Instalar dependencias:
  ```bash
  pip install requests pytest tortoise-orm
  ```
- El backend debe estar corriendo en `http://localhost:8000` para las pruebas que usan `requests`.
- Deben existir usuarios de prueba:
  - Administrador: `{ "username": "admin", "password": "adminpass" }`
  - Estudiante: `{ "username": "estu", "password": "estupass" }`
- Debe existir al menos una imagen con `id=1` en la base de datos para las pruebas de contenedores.

## Ejecución de las pruebas

### Pruebas HTTP (integración)

Desde la carpeta `backend/test` ejecuta:

```bash
python test_auth.py
python test_contenedor.py
python test_asignacion.py
```

O bien, puedes usar `pytest` para ejecutar todos los tests:

```bash
pytest
```

### Pruebas de modelos (unitarias)

Estas pruebas usan una base de datos en memoria y pueden ejecutarse con:

```bash
pytest test_models.py
```

## Notas
- Asegúrate de que el backend esté corriendo y la base de datos tenga los datos de prueba necesarios.
- Si necesitas crear los usuarios o imágenes de prueba, puedes hacerlo manualmente o agregando scripts de inicialización.
- Si algún test falla por datos inexistentes, revisa los IDs y la existencia de los recursos requeridos. 