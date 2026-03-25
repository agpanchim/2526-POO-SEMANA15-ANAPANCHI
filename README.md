# 2526-POO-SEMANA15-ANAPANCHI
La aplicación permitirá al usuario gestionar sus tareas diarias. La interfaz responde de manera fluida y natural a las interacciones del usuario, cambiando el estado visual de las tareas cuando sean completadas o eliminadas.

# Lista de Tareas

## Descripción del Proyecto
Esta aplicación es un gestor de actividades académicas desarrollado en Python utilizando la librería **Tkinter**. El sistema permite organizar tareas escolares (Exámenes, Deberes, Proyectos) asignándoles una fecha, tipo de evento, observaciones y niveles de prioridad.

La arquitectura sigue estrictamente el modelo **Modular por Capas**, separando la lógica de negocio, los modelos de datos y la interfaz gráfica para garantizar un código escalable y mantenible.

## 1. Arquitectura de Carpetas
El proyecto se organiza de la siguiente manera:
- `modelos/`: Definición de la clase `Tarea`.
- `servicios/`: Lógica para agregar, eliminar y completar tareas.
- `ui/`: Interfaz gráfica y manejo de eventos.
- `main.py`: Punto de entrada y ejecucion del sistema.

### 2. Manejo de Eventos Avanzados (Requisito Obligatorio)
Se han implementado manejadores de eventos utilizando el método `.bind()` para mejorar la experiencia de usuario:
- **Evento de Teclado (`<Return>`):** Permite añadir una tarea rápidamente presionando la tecla **Enter** mientras se escribe la descripción.
- **Evento de Ratón (`<Double-1>`):** Permite marcar una tarea como completada simplemente haciendo **doble clic** sobre ella en la lista.

### 3. Feedback Visual y Prioridades
La aplicación utiliza **Tags** en el componente `Treeview` para diferenciar las tareas:
- Rojo (Alta): Actividades urgentes.
- Amarillo (Media): Actividades pendientes de prioridad normal.
- Verde (Baja): Actividades que pueden esperar.
- Gris: Tareas finalizadas/completadas.

## Generación del Ejecutable
Para generar el archivo `.exe`, se utilizó **PyInstaller** con el siguiente comando:
```bash
pyinstaller --noconsole --onefile --name lista_tareas_app main.py