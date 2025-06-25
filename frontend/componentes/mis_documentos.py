from nicegui import ui

class mis_documentos :
    def __init__ (self, archivos) :
        
        self.archivos = archivos
        self.arbol = ui.tree(self.archivos, label_key='nombre', on_select=lambda e: ui.notify(e.value))
    
    def get_arbol(self) :
        return self.arbol
    
    def get_archivos(self) :
        return self.archivos
    
    def set_archivos(self, archivos) :
        self.arbol.__setattr__('nodes', archivos)
        self.archivos = archivos