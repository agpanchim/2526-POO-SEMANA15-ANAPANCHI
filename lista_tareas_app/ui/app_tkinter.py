# ui/app_tkinter.py
import tkinter as tk
from tkinter import ttk, messagebox
from modelos.tarea import Tarea


class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio
        self.root.title("Agenda Universitaria - Prioridades")
        self.root.geometry("800x550")  # Un poco más ancho para la tabla

        self._configurar_estilos()
        self._crear_widgets()
        self._vincular_eventos()

    def _configurar_estilos(self):
        self.style = ttk.Style()
        self.style.configure("Treeview", rowheight=25)
        # Definimos los colores para cada prioridad y estado
        # Nota: Los nombres de los tags coincidirán con los que usemos en la tabla
        self.root.option_add("*Font", "Calibri 10")

    def _crear_widgets(self):
        # --- 1. FRAME DE ENTRADA (DATOS) ---
        frame_input = tk.LabelFrame(self.root, text="Nueva Actividad Académica", padx=10, pady=10)
        frame_input.pack(pady=10, fill="x", padx=20)

        # Descripción y Fecha
        tk.Label(frame_input, text="Materia:").grid(row=0, column=0, sticky="w")
        self.ent_desc = tk.Entry(frame_input, width=30)
        self.ent_desc.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Fecha:").grid(row=0, column=2, sticky="w")
        self.ent_fecha = tk.Entry(frame_input, width=15)
        self.ent_fecha.grid(row=0, column=3, padx=5, pady=5)

        # Tipo y Prioridad
        tk.Label(frame_input, text="Tipo:").grid(row=1, column=0, sticky="w")
        self.cb_tipo = ttk.Combobox(frame_input, values=["Examen", "Deber", "Proyecto", "Taller"], state="readonly",
                                    width=27)
        self.cb_tipo.grid(row=1, column=1, padx=5, pady=5)
        self.cb_tipo.current(0)

        tk.Label(frame_input, text="Prioridad:").grid(row=1, column=2, sticky="w")
        self.cb_prioridad = ttk.Combobox(frame_input, values=["Alta", "Media", "Baja"], state="readonly", width=12)
        self.cb_prioridad.grid(row=1, column=3, padx=5, pady=5)
        self.cb_prioridad.current(1)

        tk.Label(frame_input, text="Obs:").grid(row=2, column=0, sticky="w")
        self.ent_obs = tk.Entry(frame_input, width=30)
        self.ent_obs.grid(row=2, column=1, padx=5, pady=5)

        # --- 2. FRAME DE BOTONES (ACCIONES) ---
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        # Botón Añadir (Acción principal)
        self.btn_add = tk.Button(frame_botones, text="Añadir Tarea", command=self.manejador_añadir,
                                 bg="#2ecc71", fg="white", width=15, font=("Arial", 10, "bold"))
        self.btn_add.pack(side=tk.LEFT, padx=5)

        # Botón Marcar Completada
        self.btn_complete = tk.Button(frame_botones, text="Marcar Completada", command=self.manejador_completar,
                                      bg="#3498db", fg="white", width=18)
        self.btn_complete.pack(side=tk.LEFT, padx=5)

        # Botón Eliminar (Importante para la tarea)
        self.btn_delete = tk.Button(frame_botones, text="Eliminar", command=self.manejador_eliminar,
                                    bg="#e74c3c", fg="white", width=12)
        self.btn_delete.pack(side=tk.LEFT, padx=5)

        # --- 3. TABLA (VISUALIZACIÓN) ---
        columnas = ("desc", "fecha", "tipo", "prioridad", "estado")
        self.tabla = ttk.Treeview(self.root, columns=columnas, show='headings', height=10)

        for col in columnas:
            self.tabla.heading(col, text=col.capitalize())
            self.tabla.column(col, width=110)

        self.tabla.pack(pady=10, padx=20, fill="both", expand=True)

        # Configuración de colores de las filas
        self.tabla.tag_configure("Alta", background="#ffcccc")
        self.tabla.tag_configure("Media", background="#ffffcc")
        self.tabla.tag_configure("Baja", background="#ccffcc")
        self.tabla.tag_configure("Completada", foreground="gray", background="#f0f0f0")
    def _vincular_eventos(self):
        self.ent_desc.bind("<Return>", lambda e: self.manejador_añadir())
        self.tabla.bind("<Double-1>", lambda e: self.manejador_completar())

    def actualizar_lista(self):
        # Limpiar tabla
        for i in self.tabla.get_children():
            self.tabla.delete(i)

        # Cargar tareas con tags de color
        for idx, t in enumerate(self.servicio.listar_tareas()):
            estado_texto = "Finalizado" if t.completada else "Pendiente"

            # Decidir qué tag aplicar
            if t.completada:
                tag_actual = "Completada"
            else:
                tag_actual = t.prioridad  # Usará "Alta", "Media" o "Baja"

            self.tabla.insert("", "end", iid=idx,
                              values=(t.descripcion, t.fecha, t.tipo, t.prioridad, estado_texto),
                              tags=(tag_actual,))

    def manejador_añadir(self):
        desc = self.ent_desc.get()
        fec = self.ent_fecha.get()
        tip = self.cb_tipo.get()
        prio = self.cb_prioridad.get()
        obs = self.ent_obs.get()

        if desc and fec:
            nueva = Tarea(desc, fec, tip, obs, prio)
            self.servicio.agregar_tarea(nueva)
            self.actualizar_lista()
            # Limpiar campos
            self.ent_desc.delete(0, tk.END)
            self.ent_fecha.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Completa los campos principales.")

    def manejador_completar(self):
        seleccion = self.tabla.selection()
        if seleccion:
            indice = int(seleccion[0])
            self.servicio.marcar_como_completada(indice)
            self.actualizar_lista()

    def manejador_eliminar(self):
        seleccion = self.tabla.selection()
        if seleccion:
            # Confirmación de seguridad
            res = messagebox.askyesno("Confirmar", "¿Estás segura de eliminar esta tarea académica?")
            if res:
                indice = int(seleccion[0])
                self.servicio.eliminar_tarea(indice)
                self.actualizar_lista()
        else:
            messagebox.showwarning("Atención", "Selecciona una tarea de la lista para eliminar.")