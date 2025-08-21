from componentes.router import Router
from nicegui import ui, html, app
from componentes.footer import Footer
from componentes.header import Header
from componentes.menu_lateral import MenuLateral
from componentes.mis_documentos import mis_documentos
from componentes.mis_contenedores import mis_contenedores
from config import STUDENT_ROUTE, ADMIN_ROUTE, LOGIN_ROUTE

print('[ESTUDIANTE] Archivo estudiante.py importado')

def register_routes():
    router = Router()
    usuario = {
        'nombre': 'Ramiro Sabetta',
        'rol': 'Estudiante'
    }
    opcionesMenu = {
        'Mis Documentos': lambda: router.open(mis_documentos),
        'Mis Contenedores': lambda: router.open(mis_contenedores)
    }
    columns = [
        {'name': 'nombre', 'label': 'Nombre', 'field': 'nombre', 'required': True, 'align': 'left'},
        {'name': 'descripcion', 'label': 'descripcion', 'field': 'descripcion', 'sortable': True},
        {'name': 'imagen', 'label': 'Imagen', 'field': 'imagen', 'sortable': True},
        {'name': 'estado', 'label': 'Estado', 'field': 'estado', 'sortable': True, 'align': 'center'},
        {'name': 'puertos', 'label': 'Puertos', 'field': 'puertos', 'sortable': True, 'align': 'center'},
        {'name': 'link', 'label': 'Link', 'field': 'link', 'sortable': True, 'align': 'center'},
    ]
    rows = [
        {'descripcion':'Ambiente de escritorio linux completo','nombre': 'Escritorio XFCE', 'imagen': 'webtop', 'estado':'Activo', 'puertos': 3009, 'link':'http://anexo328server:3009'},
        {'descripcion':'IDE de desarrollo','nombre': 'Visual Studio Code', 'imagen': 'code-server', 'estado':'Activo', 'puertos': 3008, 'link':'http://anexo328server:3008'},
        {'descripcion':'Modelador 3D','nombre': 'Freecad', 'imagen': 'freecad', 'estado':'Activo', 'puertos': 3000, 'link':'http://anexo328server:3000'},
        {'descripcion':'Editor de imagenes','nombre': 'Gimp', 'imagen': 'gimp', 'estado':'Activo', 'puertos':3001, 'link':'http://anexo328server:3001'},
        {'descripcion':'Editor de graficos vectoriales','nombre': 'inkscape', 'imagen': 'inkscape', 'estado':'Activo', 'puertos':3002, 'link':'http://anexo328server:3002'},
        {'descripcion':'Editor de video','nombre': 'Kdenlive', 'imagen': 'kdenlive', 'estado':'Activo', 'puertos':3005, 'link':'http://anexo328server:3005'},
        {'descripcion':'Diseñador de circuitos electronicos','nombre': 'Kicad', 'imagen': 'kicad', 'estado':'Activo', 'puertos': 3003, 'link':'http://anexo328server:3003'},
        {'descripcion':'Galeria de imagenes','nombre': 'Krita', 'imagen': 'krita', 'estado':'Activo', 'puertos': 3004, 'link':'http://anexo328server:3004'},
        {'descripcion':'Aplicaciones de Ofimatica','nombre': 'Libreoffice', 'imagen': 'libreoffice', 'estado':'Activo', 'puertos': 3006, 'link':'http://anexo328server:3006'},
    ]
    @ui.page(STUDENT_ROUTE)
    def estudiante():
        rol = app.storage.user.get('rol', '').lower()
        if rol != 'estudiante':
            if rol == 'administrador':
                ui.navigate.to(ADMIN_ROUTE)
            else:
                ui.navigate.to(LOGIN_ROUTE)
            return
        home = None
        misContenedores = None
        @router.add(STUDENT_ROUTE)
        def show_one():
            nonlocal home
            with html.section().classes('w-full justify-evenly') as main:
                with ui.row().classes('items-center justify-center p-0 m-0 gap-0 flex-col sm:flex-row ') as _home:
                    home = _home
                    ui.label('Empieza a Programar Rápido, Desde Cualquier Lugar').classes('text-center sm:text-left text-3xl lg:text-7xl md:text-5xl w-[50%] font-extrabold font-sans')
                    ui.image('./frontend/assets/logo.png').classes('w-[35%] p-0 m-0')
        @router.add('/miscontenedores')
        def mostrar_mis_contenedores():
            nonlocal misContenedores
            with ui.column().classes('w-50 justify-evenly items-center') as _misContenedores:
                misContenedores = _misContenedores
                ui.label('Mis Contenedores').classes('text-2xl')
                mis_contenedores(columns, rows)
        @router.add('/misdocumentos')
        def mis_documentos():
            ui.label('Content Three').classes('text-2xl')
        router.frame().classes('w-full p-4 bg-gray-100')
        def mostrarAlerta(texto= 'Clik!'):
            ui.notification(texto)
        def logout():
            app.storage.user.clear()
            ui.navigate.to(LOGIN_ROUTE)
        menuLateral = MenuLateral(opcionesMenu, usuario, on_logout=logout)
        header = Header(menuLateral.getMenuLateral(), None)
        header.getHeader()
        footer = Footer()
        footer.getFooter()
        ui.timer(1.0, footer.actualizarFechaHora)
        def goToHome():
            nonlocal home, misContenedores
            if home: home.set_visibility(True)
            if misContenedores: misContenedores.set_visibility(False)
            menuLateral.getMenuLateral().hide()
        def mostrarContenedores():
            nonlocal home, misContenedores
            if home: home.set_visibility(False)
            if misContenedores: misContenedores.set_visibility(True)
        menuLateral.setOpciones({'nombre': 'Mis Contenedores', 'accion': mostrarContenedores})
        header.setGoToHome(goToHome)
    # Parche para evitar KeyError en router.open
    old_open = router.open
    def safe_open(target):
        try:
            old_open(target)
        except KeyError:
            ui.navigate.to(LOGIN_ROUTE)
    router.open = safe_open