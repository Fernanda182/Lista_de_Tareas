import tkinter as tk
from ui.app_tkinter import AppListaTareas


def main():
    """
    Función principal del programa.
    Se encarga de crear la ventana y lanzar la aplicación.
    """
    root = tk.Tk()
    app = AppListaTareas(root)
    root.mainloop()


# Este bloque asegura que el archivo se ejecute solo
# cuando se lanza directamente, y no cuando se importa.
if __name__ == "__main__":
    main()