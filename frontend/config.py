# Configuración del frontend de IPAS

# Configuración del backend
BACKEND_URL = "http://192.168.192.150:3081"

# Configuración de la aplicación
APP_NAME = "IPAS"
APP_VERSION = "1.0.0"

# Configuración de autenticación
TOKEN_STORAGE_KEY = "token"
USER_STORAGE_KEY = "user"
AUTH_STORAGE_KEY = "authenticated"

# Configuración de la interfaz
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8080  # Puerto automático
STORAGE_SECRET = "THIS_NEEDS_TO_BE_CHANGED"

# Rutas de la aplicación
LOGIN_ROUTE = "/login"
ADMIN_ROUTE = "/administrador"
STUDENT_ROUTE = "/estudiante"
MAIN_ROUTE = "/"
