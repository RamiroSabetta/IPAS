#!/usr/bin/env python3
"""
Archivo principal para inicializar tanto el frontend como el backend de IPAS.
Ejecuta ambos servicios en paralelo usando subprocess.Popen.
"""

import subprocess
import sys
import os
import time
from pathlib import Path
import socket
import importlib.util

# =====================
# CONFIGURACIÓN GLOBAL
# =====================
BACKEND_HOST = "127.0.0.1"
BACKEND_PORT = 8001
BACKEND_MODULE = "main:app"  # archivo:objeto_app para uvicorn
BACKEND_DB_URL = "mysql://root:1234@192.168.1.10/ipas"

FRONTEND_HOST = "0.0.0.0"
FRONTEND_PORT = 0  # Si es 0, buscará un puerto libre automáticamente
FRONTEND_ENTRY = "login.py"  # archivo de entrada del frontend

# =====================

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((FRONTEND_HOST, 0))
        return s.getsockname()[1]

def registrar_ruta(path_modulo: Path, nombre_funcion: str = 'register_routes'):
    spec = importlib.util.spec_from_file_location(path_modulo.stem, str(path_modulo.resolve()))
    if spec is None or spec.loader is None:
        raise ImportError(f'No se pudo cargar el módulo {path_modulo}')
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    if hasattr(modulo, nombre_funcion):
        getattr(modulo, nombre_funcion)()
    else:
        raise AttributeError(f'El módulo {path_modulo} no tiene la función {nombre_funcion}')

if not Path("backend").exists():
    print("Error: No se encuentra el directorio 'backend'")
    sys.exit(1)
if not Path("frontend").exists():
    print("Error: No se encuentra el directorio 'frontend'")
    sys.exit(1)

port = FRONTEND_PORT
if port == 0:
    port = find_free_port()

try:
    backend = subprocess.Popen([
        sys.executable, "-m", "uvicorn", BACKEND_MODULE,
        "--host", BACKEND_HOST,
        "--port", str(BACKEND_PORT),
        "--reload"
    ], cwd="backend")
    time.sleep(2)
    
    # Registrar rutas de frontend de forma reutilizable
    registrar_ruta(Path('frontend') / 'login.py')
    registrar_ruta(Path('frontend') / 'estudiante.py')
    registrar_ruta(Path('frontend') / 'administrador.py')
    from nicegui import ui
    ui.run(storage_secret='THIS_NEEDS_TO_BE_CHANGED', host=FRONTEND_HOST, port=port)
    backend.wait()

except KeyboardInterrupt:
    backend.terminate()
    backend.wait()
except Exception as e:
    try:
        backend.terminate()
    except:
        pass

