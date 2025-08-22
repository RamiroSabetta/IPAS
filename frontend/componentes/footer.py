from nicegui import ui
from assets import funcion_hora

class Footer:
    def __init__(self):

        with ui.footer().classes('w-full p-1 justify-between items-center h-12') as self.footer:
            ui.label('Diseñado y Desarrollado por Marcos García y Ramiro Sabetta').classes('text-sm ml-[10px]')
            with ui.column().classes('gap-0 p-1 justify-end mr-[10px]') as self.contenedorFechaHora:
                self.labelHora = ui.label().classes('text-[12px] text-black font-bold')
                self.labelFecha = ui.label().classes('text-[12px] text-black font-bold')

    def getFooter(self):
        return self.footer
    
    def actualizarFechaHora(self):
            self.labelHora.text = funcion_hora.obtenerHora()
            self.labelFecha.text = funcion_hora.obtenerFecha()
            
    