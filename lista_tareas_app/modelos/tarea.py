# modelos/tarea.py

class Tarea:
    def __init__(self, descripcion, fecha, tipo, observacion, prioridad):
        self.descripcion = descripcion
        self.fecha = fecha
        self.tipo = tipo
        self.observacion = observacion
        self.prioridad = prioridad  # "Alta", "Media", "Baja"
        self.completada = False