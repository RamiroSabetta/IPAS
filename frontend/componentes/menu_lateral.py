from nicegui import ui

class MenuLateral:
    def __init__(self, opciones, usuario, on_logout=None):
        self.botones = {}
        self.opciones = opciones
        with ui.left_drawer(value=False).classes('bg-blue-300 items-center justify-evenly z-40').props('overlay') as self.menuLateral:
            
            with ui.column() as contenedorBotones:
                for opcion in opciones.keys():
                    self.botones[opcion] = ui.button(opcion, on_click= lambda: self.click(opcion)).classes('w-[180px] h-auto text-center items-center')

            ui.separator()

            with ui.column().classes('items-center') as contenedorUsuario:
                ui.icon('person', color='white').classes('text-[8em]')

            with ui.column().classes('items-center justify-center') as contenedorInfoUsuario:
                ui.label(usuario['nombre']).classes('w-[180px] text-center border-2 pt-2 pb-2 rounded-sm border-[#B8E1FF] font-bold')
                ui.label(usuario['rol']).classes('w-[180px] text-center border-2 pt-2 pb-2 rounded-sm border-[#B8E1FF] font-bold')

            with ui.column() as contenedorBoton:
                ui.button('Cerrar Sesión', on_click=on_logout).classes('w-[180px] h-auto text-center items-center text-black')
                

    def setOpciones(self, opcion):
        self.opciones[opcion['nombre']]= opcion['accion']
        

    def getMenuLateral(self):
        return self.menuLateral

    def click(self, accion):
        self.opciones[accion]()
        self.menuLateral.hide()
