#  Aplicación Lista de Tareas

# Autor:
Fernanda Vaca

##  Descripción
Este proyecto consiste en el desarrollo de una aplicación de escritorio tipo "Lista de Tareas" utilizando Python y la librería Tkinter. La aplicación permite gestionar tareas diarias de manera interactiva, aplicando eventos de usuario y una arquitectura modular por capas.


##  Tecnologías utilizadas
- Python 
- Tkinter (interfaz gráfica)
- PyInstaller (para generar ejecutable)


##  Arquitectura del proyecto
El sistema está organizado en capas, separando responsabilidades:

- **modelos/** → Define la estructura de los datos (clase Tarea)
- **servicios/** → Contiene la lógica de negocio (gestión de tareas)
- **ui/** → Maneja la interfaz gráfica (Tkinter)
- **main.py** → Punto de entrada de la aplicación


##  Funcionalidades
- Agregar nuevas tareas
- Marcar tareas como completadas
- Eliminar tareas
- Visualización de tareas con estado (Pendiente / Hecho)
- Interacción mediante eventos (click, teclado, doble clic)


##  Estructura del proyecto
LISTA_TAREAS_APP/
│
├── main.py
├── modelos/
│   └── tarea.py
├── servicios/
│   └── tarea_servicio.py
├── ui/
│   └── app_tkinter.py


##   Notas
Se utilizó programación orientada a objetos (POO)
Se aplicó inyección de dependencias en la interfaz
Se respetó la separación entre lógica de negocio y presentación
No se utilizaron librerías externas (solo estándar de Python)
