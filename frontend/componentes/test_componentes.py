from nicegui import ui

from mis_documentos import mis_documentos

archivos = [
    
    {'id': '1', 'nombre': 'Archivos de programación', 'descripcion' : 'Directorio que contiene archivos de programación',
     
    'children': 
    
        [{'id': '1A', 'nombre' : 'holaMundo.js', 'descripcion' : 'Un archivo JS'}, 
        
        {'id': '2A' , 'nombre' : 'hola.txt', 'descripcion' : 'Un archivo TXT'}]},
    
    
    {'id': '2', 'nombre': 'Fotos', 'descripcion' : 'Directorio que contiene fotos',

    'children': 
        
        [{'id': 'A', 'nombre' : 'auto.png'}, 
        
        {'id': 'B', 'nombre' : 'moto.jpg'}]},
]

misDocumentos = mis_documentos(archivos)

misDocumentos.get_arbol()

ui.run()