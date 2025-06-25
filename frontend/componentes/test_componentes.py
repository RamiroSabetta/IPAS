from nicegui import ui

from mis_documentos import mis_documentos

archivos = [
    
    {'id': '1', 'nombre': 'Archivos de programación',
     
    'children': 
    
        [{'id': '1A', 'nombre' : 'holaMundo.js'}, 
        
        {'id': '2A' , 'nombre' : 'hola.txt'}]},
    
    
    {'id': '2', 'nombre': 'Fotos', 

    'children': 
        
        [{'id': 'A', 'nombre' : 'auto.png'}, 
        
        {'id': 'B', 'nombre' : 'moto.jpg'}]},
]

misDocumentos = mis_documentos(archivos)

misDocumentos.get_arbol()

ui.run()