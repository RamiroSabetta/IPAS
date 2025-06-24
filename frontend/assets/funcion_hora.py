from datetime import datetime

def obtenerHora():
    ahora = datetime.now()
    return f'Hora: {ahora.strftime("%H:%M:%S")}'

def obtenerFecha():
    ahora = datetime.now()
    return f'Fecha: {ahora.strftime("%d/%m/%Y")}'
