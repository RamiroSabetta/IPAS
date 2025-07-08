from nicegui import ui

ESTILOS_DESCARGAR = 'w-fit text-[11px] bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center'
ESTILOS_RENOMBRAR = 'w-fit text-[11px] bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center'
ESTILOS_ELIMINAR = 'w-fit text-[11px] bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center'
ESTILOS_CONTENEDOR = 'flex gap-4 mt-4'

class mis_documentos :
    def __init__ (self, archivos) :
        
        self.archivos = archivos
        self.arbol = ui.tree(self.archivos, label_key='nombre')
        
        self.arbol.add_slot('default-body', f'''<span :props="props">Descripción: {{{{ props.node.descripcion }}}}</span>
        <span class='{ESTILOS_CONTENEDOR}'>
        <button title="Descargar" class="{ESTILOS_DESCARGAR}"><svg class="fill-current w-4 h-4 mr-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M13 8V2H7v6H2l8 8 8-8h-5zM0 18h20v2H0v-2z"/></svg></button>
        <button title="Renombrar" class="{ESTILOS_RENOMBRAR}"><svg class="fill-current w-4 h-4 mr-1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M17.414 2.586a2 2 0 0 0-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 0 0 0-2.828zM3 17h14v2H3v-2z"/></svg></button>
        <button title="Eliminar" class="{ESTILOS_ELIMINAR}"><svg class="fill-current w-4 h-4 mr-1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M6 2a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v1h5v2H0V3h5V2zm1 5h2v9H7V7zm4 0h2v9h-2V7z"/></svg></button>
        </span>''')

        ui.input('filtrar').bind_value_to(self.arbol, 'filter')
    
    def get_arbol(self) :
        return self.arbol
    
    def get_archivos(self) :
        return self.archivos
    
    def set_archivos(self, archivos) :
        self.arbol.__setattr__('nodes', archivos)
        self.archivos = archivos