from config import ADMIN_ROUTE, STUDENT_ROUTE, LOGIN_ROUTE

class Helpers:
    def __init__(self):
        pass

    def verificar_rol_admin(self, app, ui ):
        print('[ADMIN] Entrando a la función main() de administrador')
        rol = app.storage.user.get('rol', '').lower()
        if rol != 'admin':
            if rol == 'estudiante':
                ui.navigate.to(STUDENT_ROUTE)
            else:
                ui.navigate.to(LOGIN_ROUTE)
            return