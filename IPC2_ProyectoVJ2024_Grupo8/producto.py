
class Producto:
    def __init__(self, producto_id, nombre, precio, descripcion, categoria, cantidad, imagen):
        self.producto_id = producto_id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.categoria = categoria
        self.cantidad = cantidad
        self.imagen = imagen
        self.next = None
        self.prev = None

class ListaCircularDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def adjuntar(self, producto):
        if not isinstance(producto, Producto):
            raise ValueError("Debe ser una instancia de producto")

        if self.cabeza is None:
            self.cabeza = producto
            self.cabeza.next = self.cabeza.prev = self.cabeza
        else:
            cola = self.cabeza.prev
            cola.next = producto
            producto.prev = cola
            producto.next = self.cabeza
            self.cabeza.prev = producto

    def mostrar(self):
        if self.cabeza is None:
            return
        actual = self.cabeza
        while True:
            print(f'ID: {actual.producto_id}, Nombre: {actual.nombre}, Precio: {actual.precio}, Descrición: {actual.descripcion}, Categoría: {actual.categoria}, Cantidad: {actual.cantidad}, Imagen: {actual.imagen}')
            actual = actual.next
            if actual == self.cabeza:
                break


ListaProductos = ListaCircularDoblementeEnlazada()
ListaProductos.adjuntar(Producto("IPCM-1", "Leche", 10.0, "Leche de vaca", "Lacteos", 2, "leche.png"))
ListaProductos.adjuntar(Producto("IPCM-2", "Pan", 20.0, "Pan blanco", "Panaderia", 4, "pan.png"))
ListaProductos.mostrar()
