class Actividades:
    def __init__(self, actividad_id, nombre, descripcion, empleado_id, dia, hora):
        self.actividad_id = actividad_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleado_id = empleado_id
        self.dia = dia
        self.hora = hora
        self.right = None
        self.down = None

class ListaOrtogonal:
    def __init__(self):
        self.dias = [None] * 7  # Lunes a domingo
        self.horas = [None] * 24  # De 0 a 23 horas

    def insertar(self, actividad):
        dia = actividad.dia - 1  # Convierte a índice basado en 0
        hora = actividad.hora

        # Inserta en la lista de días
        if self.dias[dia] is None:
            self.dias[dia] = actividad
        else:
            actual = self.dias[dia]
            while actual.down and actual.hora < hora:
                actual = actual.down
            if actual.hora == hora:
                actual.right = actividad
            else:
                actividad.down = actual.down
                actual.down = actividad

        # Inserta en la lista de horas
        if self.horas[hora] is None:
            self.horas[hora] = actividad
        else:
            actual = self.horas[hora]
            while actual.right and actual.dia < dia:
                actual = actual.right
            if actual.dia == dia:
                actual.down = actividad
            else:
                actividad.right = actual.right
                actual.right = actividad

    def mostrar(self):
        for dia in range(7):
            print(f'Día {dia + 1}:')
            actual = self.dias[dia]
            while actual:
                print(f'  Hora: {actual.hora}, {actual.nombre} - {actual.descripcion}')
                actual = actual.down


ListaActividades = ListaOrtogonal()
ListaActividades.insertar(Actividades("A1", "Reunión", "Reunion con los empleados y Jefes", "E1", 1, 8))
ListaActividades.insertar(Actividades("A2", "Cerrar tienda", "Arreglar y dejar limpio todo", "E2", 1, 22))
ListaActividades.insertar(Actividades("A3", "Entregas", "Recibir mercaderia nueva", "E1", 4, 11))
ListaActividades.mostrar()
