from nicegui import ui

ESTILOS_DESCARGAS = 'text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800'

class mis_documentos :
    def __init__ (self, archivos) :
        
        self.archivos = archivos
        self.arbol = ui.tree(self.archivos, label_key='nombre')
        
        self.arbol.add_slot('default-body', f''' <span :props="props">Descripción: {{ props.node.descripcion }}</span> <button class="{ESTILOS_DESCARGAS}">Hola</button> ''')
        ui.input('filtrar').bind_value_to(self.arbol, 'filter')
    
    def get_arbol(self) :
        return self.arbol
    
    def get_archivos(self) :
        return self.archivos
    
    def set_archivos(self, archivos) :
        self.arbol.__setattr__('nodes', archivos)
        self.archivos = archivos