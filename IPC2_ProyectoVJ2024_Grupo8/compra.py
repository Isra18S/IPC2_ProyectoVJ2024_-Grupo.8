
class SolicitudCompra:
    def __init__(self, usuario_id, usuarioNombre, productos, total):
        self.usuario_id = usuario_id
        self.usuarioNombre = usuarioNombre
        self.productos = productos
        self.total = total
        self.next = None

class Cola:
    def __init__(self):
        self.front = None
        self.rear = None

    def PonerCola(self, solicitud):
        if not isinstance(solicitud, SolicitudCompra):
            raise ValueError("Debe ser una instancia de Solicitud de compra")
        
        if self.rear is None:
            self.front = self.rear = solicitud
        else:
            self.rear.next = solicitud
            self.rear = solicitud

    def QuitarCola(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp

    def mostrar(self):
        actual = self.front
        while actual:
            print(f'ID usuario: {actual.usuario_id}, Nombre del Usuario: {actual.usuarioNombre}, Total: {actual.total}')
            actual = actual.next

CompraCola = Cola()
CompraCola.PonerCola(SolicitudCompra("1", "Supa", ["Leche", "Pan"], 30.0))
CompraCola.PonerCola(SolicitudCompra("2", "Joni", ["Huevos", "Jugo", "Vino"], 70.0))
CompraCola.mostrar()

class ListaSimplementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def adjuntar(self, solicitud):
        if not isinstance(solicitud, SolicitudCompra):
            raise ValueError("Debe ser una instancia de compra.")
        
        if self.cabeza is None:
            self.cabeza = solicitud
        else:
            actual = self.cabeza
            while actual.next:
                actual = actual.next
            actual.next = solicitud

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(f'ID usuario: {actual.usuario_id}, Nombre usuario: {actual.usuarioNombre}, Total: {actual.total}')
            actual = actual.next


accepted_purchases = ListaSimplementeEnlazada()
accepted_purchases.adjuntar(SolicitudCompra("1", "Supa", ["Leche", "Pan"], 30.0))
accepted_purchases.adjuntar(SolicitudCompra("2", "Joni", ["Huevos", "Jugo", "Vino"], 70.0))
accepted_purchases.mostrar()
