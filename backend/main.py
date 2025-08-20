"""
YAML-to-Backend - Punto de entrada principal

Este archivo permite personalizar la configuración del backend
y ejecutar la aplicación de forma simple. 
"""

# =============================================================================
# IMPORTS
# =============================================================================

import sys
import os

# Agregar el directorio raíz al path para que funcione desde tests/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from yaml_to_backend import update_config, get_run_backend

# =============================================================================
# CONFIGURACIÓN PERSONALIZADA
# =============================================================================
# Aquí puedes modificar cualquier valor de configuración por defecto
# Descomenta y modifica las líneas que necesites:

# Ejemplo: Cambiar el puerto del servidor
# update_config(PORT=8002)

# Ejemplo: Cambiar configuración de base de datos
update_config(
    ENTITIES_PATH='./entidades/',  # Usar el directorio de entidades en tests
    DB_HOST='mariadb',
    DB_USER='root',
    DB_PASSWORD='1234',
    DB_NAME='ipas',
    DB_PORT=3306,
    PORT=8080,
    INSTALL=True,
    DEBUG=True,
    LOG=True,
    AUTH={
        'tabla': 'usuarios',
        'columna_usuario': 'nombre',  # Cambiado de 'username' a 'nombre' para coincidir con el YAML
        'columna_password': 'password',
        'superusuario': 'admin',
        'password_default': 'admin123',
        'columna_borrado': 'habilitado',
        'borrado_logico': 'boolean'
    }
)

# Ejemplo: Agregar usuarios iniciales
update_config(
    INITIAL_USERS=[
        {'nombre': 'admin', 'password': 'admin123', 'rol': 'admin', 'habilitado': True, 'email': 'admin@ejemplo.com'},
        {'nombre': 'estudiante', 'password': 'estudiante123', 'rol': 'estudiante', 'habilitado': True, 'email': 'estudiante@ejemplo.com'},
        {'nombre': 'desarrollador', 'password': 'dev123', 'rol': 'admin', 'habilitado': True, 'email': 'dev@ejemplo.com'}
    ]
)

# =============================================================================
# EJECUCIÓN DEL BACKEND
# =============================================================================

if __name__ == "__main__":
    # Ejecutar el backend
    run_backend = get_run_backend()
    run_backend() 