#!/usr/bin/env python3
from frontend.componentes.router import Router

from nicegui import app, ui

print('[ADMIN] Archivo administrador.py importado')

def register_routes():
    @ui.page('/administrador')
    def main():
        print('[ADMIN] Entrando a la función main() de administrador')
        perfil = app.storage.user.get('perfil', '').lower()
        if perfil != 'administrador':
            if perfil == 'estudiante':
                ui.navigate.to('/estudiante')
            else:
                ui.navigate.to('/login')
            return
        router = Router()
        @router.add('/')
        def show_one():
            ui.label('Content One').classes('text-2xl')
        @router.add('/two')
        def show_two():
            ui.label('Content Two').classes('text-2xl')
        @router.add('/three')
        def show_three():
            ui.label('Content Three').classes('text-2xl')
        with ui.row():
            ui.button('One', on_click=lambda: router.open(show_one)).classes('w-32')
            ui.button('Two', on_click=lambda: router.open(show_two)).classes('w-32')
            ui.button('Three', on_click=lambda: router.open(show_three)).classes('w-32')
        router.frame().classes('w-full p-4 bg-gray-100')