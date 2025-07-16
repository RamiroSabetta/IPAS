from nicegui import ui
from frontend.assets import funcion_hora

class Footer:
    def __init__(self):

        with ui.footer().classes('w-full p-1 justify-between items-center h-12') as self.footer:
            ui.label('Diseñado y desarrollado por Marcos García y Ramiro Sabetta').classes('text-sm')
            with ui.column().classes('gap-0 p-1 justify-end') as self.contenedorFechaHora:
                self.labelHora = ui.label().classes('text-black')
                self.labelFecha = ui.label().classes('text-black')

    def getFooter(self):
        return self.footer
    
    def actualizarFechaHora(self):
            self.labelHora.text = funcion_hora.obtenerHora()
            self.labelFecha.text = funcion_hora.obtenerFecha()
            
    