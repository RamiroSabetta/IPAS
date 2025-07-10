from componentes.router import Router
from nicegui import ui, html
from componentes.footer import Footer
from componentes.header import Header
from componentes.menu_lateral import MenuLateral

@ui.page('/')  # normal index page (e.g. the entry point of the app)
@ui.page('/{_:path}')  # all other pages will be handled by the router but must be registered to also show the SPA index page

def estudiante():
    router = Router()

    @router.add('/')
    def show_one():
        with html.section().classes('w-full justify-evenly') as main:
    
            with ui.row().classes('items-center justify-center p-0 m-0 gap-0 flex-col sm:flex-row ') as home:
                ui.label('Empieza a Programar Rápido, Desde Cualquier Lugar').classes('text-center sm:text-left text-3xl lg:text-7xl md:text-5xl w-[50%] font-extrabold font-sans')
                
                ui.image('./assets/logo.png').classes('w-[35%] p-0 m-0')

    @router.add('/miscontenedores')
    def mis_contenedores():
        ui.label('Content Two').classes('text-2xl')

    @router.add('/misdocumentos')
    def mis_documentos():
        ui.label('Content Three').classes('text-2xl')

    # this places the content which should be displayed
    router.frame().classes('w-full p-4 bg-gray-100')

def mostrarAlerta(texto= 'Clik!'):
    ui.notification(texto)

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

menuLateral = MenuLateral(opcionesMenu, usuario)
header = Header(menuLateral.getMenuLateral(), None)
header.getHeader()

with html.section().classes('w-full justify-evenly') as main:
    
    with ui.row().classes('items-center justify-center p-0 m-0 gap-0 flex-col sm:flex-row ') as home:
        ui.label('Empieza a Programar Rápido, Desde Cualquier Lugar').classes('text-center sm:text-left text-3xl lg:text-7xl md:text-5xl w-[50%] font-extrabold font-sans')
        
        ui.image('./Frontend/Images/Logo.png').classes('w-[35%] p-0 m-0')
    
    with ui.column().classes('w-50 justify-evenly items-center') as misContenedores:
        contenedores = ui.table(columns=columns, rows=rows, row_key='nombre').classes('text-black text-center')
        contenedores.add_slot('body-cell-estado', '''
            <q-td :props="props">
                <q-badge :color="props.value == 'Detenido' ? 'red' : 'green'">
                    {{ props.value }}
                </q-badge>
            </q-td>
        ''')
        contenedores.add_slot('body-cell-link', '''
            <q-td :props="props">
                <a :href="props.value" target="_blank" v-if="props.value">ABRIR</a>
            </q-td>
        ''')
    
misContenedores.set_visibility(visible=False)
footer = Footer()
footer.getFooter()
ui.timer(1.0, footer.actualizarFechaHora)

def goToHome():
    home.set_visibility(visible=True)
    misContenedores.set_visibility(visible=False)
    menuLateral.getMenuLateral().hide()

def mostrarContenedores():
    home.set_visibility(visible=False)
    misContenedores.set_visibility(visible=True)

menuLateral.setOpciones({'nombre': 'Mis Contenedores', 'accion': mostrarContenedores})

header.setGoToHome(goToHome)

estudiante()
ui.run()