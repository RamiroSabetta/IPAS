from nicegui import ui, html

class Header:
    def __init__(self, menuLateral_, home):
        self.home = home
        with ui.header().classes('items-center p-0') as self.header:
            ui.button(on_click=menuLateral_.toggle, icon='menu').props('flat color=white')
            with ui.row().classes('w-[90dvw] items-center justify-between'):
                with ui.button(on_click=self.home).props('unelevated') as self.irHome:
                    html.h1('IPAS').classes('text-5xl font-extrabold font-sans')
                ui.html('<h2>Infraestructura, Plataforma, Ambiente y Servicio</h2>').classes('text-lg text-gray-600 italic ml-[10px] font-extrabold')

    def getHeader(self):
        return self.header
    
    def setGoToHome(self, home):
        self.home=home
        self.irHome.on_click(home)