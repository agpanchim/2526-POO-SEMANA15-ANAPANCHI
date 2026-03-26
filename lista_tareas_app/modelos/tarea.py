# modelos/tarea.py

class Tarea:
    def __init__(self, descripcion, fecha, tipo, observacion, prioridad):
        self.descripcion = descripcion
        self.fecha = fecha
        self.tipo = tipo
        self.observacion = observacion
        self.prioridad = prioridad  # "Alta", "Media", "Baja"
        self.completada = False

        # --- GETTERS (Para obtener el valor) ---
        @property
        def descripcion(self):
            return self._descripcion

        @property
        def fecha(self):
            return self._fecha

        @property
        def tipo(self):
            return self._tipo

        @property
        def observacion(self):
            return self._observacion

        @property
        def prioridad(self):
            return self._prioridad

        @property
        def completada(self):
            return self._completada

        # --- SETTERS (Para modificar el valor) ---
        @descripcion.setter
        def descripcion(self, valor):
            self._descripcion = valor

        @completada.setter
        def completada(self, valor):
            self._completada = valor
