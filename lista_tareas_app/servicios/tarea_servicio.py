# servicios/tarea_servicio.py

class TareaServicio:
    """
    Capa de Lógica de Negocio: Gestiona las operaciones de la agenda
    sin conocer la interfaz gráfica (UI).
    """
    def __init__(self):
        # Lista privada para almacenar objetos de la clase Tarea
        self._tareas = []

    def agregar_tarea(self, tarea_objeto):
        """
        Recibe un objeto de tipo Tarea y lo añade a la colección.
        """
        if tarea_objeto.descripcion.strip():
            self._tareas.append(tarea_objeto)
            return True
        return False

    def marcar_como_completada(self, indice):
        """
        Cambia el estado de una tarea específica basada en su posición.
        """
        if 0 <= indice < len(self._tareas):
            self._tareas[indice].completada = True
            return True
        return False

    def eliminar_tarea(self, indice):
        """
        Elimina una tarea de la lista por su índice.
        """
        if 0 <= indice < len(self._tareas):
            self._tareas.pop(indice)
            return True
        return False

    def listar_tareas(self):
        """
        Retorna la lista completa de tareas para ser visualizadas.
        """
        return self._tareas