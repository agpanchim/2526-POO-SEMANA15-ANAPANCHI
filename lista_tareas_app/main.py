# main.py
import tkinter as tk
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTkinter


def main():
    """
    Función principal, Separa la creación del servicio (Lógica) de la ventana (UI).
    """
    # Crea la raíz de la aplicación Tkinter
    root = tk.Tk()

    # Capa de servicios (Lógica de negocio)
    # Esta capa no sabe nada de botones ni etiquetas, solo gestiona datos.
    servicio = TareaServicio()

    # Interfaz gráfica enviándole el servicio
    # La UI usará los métodos del servicio para añadir o completar tareas.
    app = AppTkinter(root, servicio)

    # Inicia el bucle principal de eventos
    # Esto mantiene la ventana abierta y escuchando clics/teclas.
    root.mainloop()


if __name__ == "__main__":
    main()