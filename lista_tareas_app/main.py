# main.py
import tkinter as tk
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTkinter


def main():
    root = tk.Tk()          # Crea la raíz de la aplicación Tkinter
    servicio = TareaServicio()  # Capa de servicios (Lógica de negocio)
    app = AppTkinter(root, servicio)        # Interfaz gráfica enviándole el servicio
    root.mainloop()     # Inicia el bucle

if __name__ == "__main__":
    main()
