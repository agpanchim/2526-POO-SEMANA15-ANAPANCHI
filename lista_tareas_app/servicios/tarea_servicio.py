# servicios/tarea_servicio.py

class TareaServicio:
    """
    Capa de Lógica: Gestiona las operaciones de la agenda sin conocer la interfaz gráfica (UI).
    """

    def __init__(self):
        # Lista privada para almacenar objetos de la clase Tarea
        self._tareas = []

    def agregar_tarea(self, tarea_objeto):
        if tarea_objeto.descripcion.strip():
            self._tareas.append(tarea_objeto)
            return True
        return False

    def marcar_como_completada(self, indice):
        if 0 <= indice < len(self._tareas):
            self._tareas[indice].completada = True
            return True
        return False

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self._tareas):
            self._tareas.pop(indice)
            return True
        return False

    def listar_tareas(self):
         return self._tareas
