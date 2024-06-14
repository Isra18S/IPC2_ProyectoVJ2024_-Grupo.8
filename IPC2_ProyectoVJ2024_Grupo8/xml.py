import xml.etree.ElementTree as ET
from usuario import ListaDoblementeEnlazada

#AUN NO SIRVE XD

def CargarUsuariosXML(RutaArchivo, ListaUsuarios):
    tree = NuevaFuncion(RutaArchivo)
    root = tree.getroot()
    
    for usuario in root.findall('usuario'):
        usuario_id = usuario.find('ID').text
        nombre = usuario.find('nombre').text
        edad = int(usuario.find('edad').text)
        email = usuario.find('email').text
        telefono = usuario.find('telefono').text
        
        ListaUsuarios.adjuntar(usuario(usuario_id, nombre, edad, email, telefono))

def NuevaFuncion(file_path):
    return ET.parse(file_path)

ListaUsuarios = ListaDoblementeEnlazada()
CargarUsuariosXML('usuarios.xml', ListaUsuarios)
ListaUsuarios.mostrar()
