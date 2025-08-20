#!/usr/bin/env python3
"""
Archivo principal para inicializar el frontend de IPAS.
Ejecuta solo el servicio frontend usando NiceGUI.
"""

import sys
import socket
from pathlib import Path
import importlib.util
from config import DEFAULT_HOST, DEFAULT_PORT, STORAGE_SECRET

# =====================
# CONFIGURACIÓN GLOBAL
# =====================
FRONTEND_HOST = DEFAULT_HOST
FRONTEND_PORT = DEFAULT_PORT
FRONTEND_ENTRY = "login.py"  # archivo de entrada del frontend

# =====================

def find_free_port():
    """Encuentra un puerto libre disponible."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((FRONTEND_HOST, 0))
        return s.getsockname()[1]

def registrar_ruta(path_modulo: Path, nombre_funcion: str = 'register_routes'):
    """Registra las rutas de un módulo del frontend."""
    spec = importlib.util.spec_from_file_location(path_modulo.stem, str(path_modulo.resolve()))
    if spec is None or spec.loader is None:
        raise ImportError(f'No se pudo cargar el módulo {path_modulo}')
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    if hasattr(modulo, nombre_funcion):
        getattr(modulo, nombre_funcion)()
    else:
        raise AttributeError(f'El módulo {path_modulo} no tiene la función {nombre_funcion}')

def main():
    """Función principal que inicia el frontend."""
    # Verificar que existe el directorio frontend (ahora estamos dentro de él)
    if not Path(".").exists():
        print("Error: No se puede acceder al directorio actual")
        sys.exit(1)

    # Encontrar puerto libre si no se especifica uno
    port = FRONTEND_PORT
    if port == 0:
        port = find_free_port()
        print(f"Puerto asignado automáticamente: {port}")

    try:
        print("Iniciando frontend de IPAS...")
        
        # Registrar rutas de frontend de forma reutilizable
        # Ahora las rutas son relativas al directorio actual (frontend)
        print("Registrando rutas del frontend...")
        registrar_ruta(Path('login.py'))
        registrar_ruta(Path('estudiante.py'))
        registrar_ruta(Path('administrador.py'))
        
        # Iniciar la aplicación NiceGUI
        from nicegui import ui
        print(f"Frontend iniciado en http://{FRONTEND_HOST}:{port}")
        ui.run(storage_secret=STORAGE_SECRET, host=FRONTEND_HOST, port=port)

    except KeyboardInterrupt:
        print("\nAplicación terminada por el usuario")
    except Exception as e:
        print(f"Error al iniciar el frontend: {e}")
        sys.exit(1)

if __name__ in {"__main__", "__mp_main__"}:
    main()

