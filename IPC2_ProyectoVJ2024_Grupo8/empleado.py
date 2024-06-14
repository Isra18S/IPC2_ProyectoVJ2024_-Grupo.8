class Empleados:
    def __init__(self, codigo, nombre, puesto):
        self.codigo = codigo
        self.nombre = nombre
        self.puesto = puesto
        self.next = None

class ListaCircularSimplenteEnlazada:
    def __init__(self):
        self.cabeza = None

    def adjuntar(self, empleado):
        if not isinstance(empleado, Empleados):
            raise ValueError("Debe ser una instancia de empleado")

        if self.cabeza is None:
            self.cabeza = empleado
            self.cabeza.next = self.cabeza
        else:
            actual = self.cabeza
            while actual.next != self.cabeza:
                actual = actual.next
            actual.next = empleado
            empleado.next = self.cabeza

    def mostrar(self):
        if self.cabeza is None:
            return
        actual = self.cabeza
        while True:
            print(f'Código: {actual.codigo}, Nombre: {actual.nombre}, Puesto: {actual.puesto}')
            actual = actual.next
            if actual == self.cabeza:
                break


ListaEmpleados = ListaCircularSimplenteEnlazada()
ListaEmpleados.adjuntar(Empleados("E-1", "Paola Contreras", "Vendedora"))
ListaEmpleados.adjuntar(Empleados("E-2", "Israel Gallina", "Vendedor"))
ListaEmpleados.mostrar()
