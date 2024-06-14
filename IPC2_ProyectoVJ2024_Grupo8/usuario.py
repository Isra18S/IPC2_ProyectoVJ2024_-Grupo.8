
class Usuario:
    def __init__(self, user_id, nombre, edad, email, telefono):
        self.user_id = user_id
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.telefono = telefono
        self.next = None
        self.prev = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def adjuntar(self, usuario):
        if not isinstance(usuario, Usuario):
            raise ValueError("Debe ser una instancia de usuario")
        
        if self.cabeza is None:
            self.cabeza = self.cola = usuario
        else:
            self.cola.next = usuario
            usuario.prev = self.cola
            self.cola = usuario

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(f'ID: {actual.user_id}, Nombre: {actual.nombre}, Edad: {actual.edad}, E-mail: {actual.email}, Teléfono: {actual.telefono}')
            actual = actual.next


ListaUsuarios = ListaDoblementeEnlazada()
ListaUsuarios.adjuntar(Usuario("1", "Susana González", 23, "susipaolagc@gmail.com", "12345678"))
ListaUsuarios.adjuntar(Usuario("2", "Jonathan Solís", 20, "joni@gmail.com", "87654321"))
ListaUsuarios.mostrar()
