#!/usr/bin/env python3
from typing import Optional
import requests
from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

from nicegui import app, ui

unrestricted_page_routes = {'/login'}

BACKEND_URL = "http://localhost:8000"


class AuthMiddleware(BaseHTTPMiddleware):
    """This middleware restricts access to all NiceGUI pages.

    It redirects the user to the login page if they are not authenticated.
    """

    async def dispatch(self, request: Request, call_next):
        if not app.storage.user.get('authenticated', False):
            if not request.url.path.startswith('/_nicegui') and request.url.path not in unrestricted_page_routes:
                return RedirectResponse(f'/login?redirect_to={request.url.path}')
        return await call_next(request)


app.add_middleware(AuthMiddleware)


@ui.page('/')
def main_page() -> None:
    def logout() -> None:
        app.storage.user.clear()
        ui.navigate.to('/login')

    with ui.column().classes('absolute-center items-center'):
        ui.label(f'Hello {app.storage.user["username"]}!').classes('text-2xl')
        ui.button(on_click=logout, icon='logout').props('outline round')


@ui.page('/subpage')
def test_page() -> None:
    ui.label('This is a sub page.')

@ui.page('/login')
def login(redirect_to: str = '/') -> Optional[RedirectResponse]:
    def try_login() -> None:
        data = {"username": username.value, "password": password.value}
        try:
            response = requests.post(f"{BACKEND_URL}/login", json=data)
            if response.status_code == 200:
                token = response.json()["access_token"]
                headers = {"Authorization": f"Bearer {token}"}
                me_response = requests.get(f"{BACKEND_URL}/me", headers=headers)
                if me_response.status_code == 200:
                    perfil = me_response.json().get("perfil", "")
                    app.storage.user.update({
                        'username': username.value,
                        'authenticated': True,
                        'token': token,
                        'perfil': perfil
                    })
                    if perfil.lower() == 'administrador':
                        ui.navigate.to('/administrador')
                    else:
                        ui.navigate.to('/estudiante')
                else:
                    ui.notify('No se pudo obtener el perfil del usuario', color='negative')
            else:
                ui.notify('Usuario o contraseña incorrectos', color='negative')
        except Exception as e:
            ui.notify(f'Error de conexión: {e}', color='negative')
    
    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/')
    with ui.row().classes('justify-center items-center self-center pt-14'):
        ui.label('IPAS').classes('text-4xl italic')
        ui.image('./Frontend/Images/Logo.png').classes('w-20')
        
    with ui.card().classes('absolute-center gap-10'):
        
        with ui.column().classes('self-start'):
            username = ui.input('Nombre de usuario', validation={'El valor del campo excede el máximo de carácteres': lambda value: len(value) < 50}).on('keydown.enter', try_login)
            password = ui.input('Contraseña', password=True, password_toggle_button=True).on('keydown.enter', try_login)
        
        with ui.column().classes('items-center self-center') as contenedorBotones:
            ui.button('INICIAR SESIÓN', on_click=try_login)
            ui.button('Olvidé mis datos', on_click=lambda: ui.notify('Para recuperar tu nombre de Usuario y/o Contraseña contacta a un Administrador', close_button='OK', position='top'))
    return None

if __name__ in {'__main__', '__mp_main__'}:
    ui.run(storage_secret='THIS_NEEDS_TO_BE_CHANGED')