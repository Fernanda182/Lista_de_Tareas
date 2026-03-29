class Tarea:
    """
    Esta clase representa una tarea individual dentro de la aplicación.
    Cada tarea tendrá:
    - un id único
    - una descripción
    - un estado que indica si está completada o no
    """

    def __init__(self, id_tarea, descripcion, completada=False):
        # Guardamos el identificador de la tarea
        self.id = id_tarea

        # Guardamos el texto o descripción de la tarea
        self.descripcion = descripcion

        # Guardamos si la tarea está completada o no
        self.completada = completada

    def marcar_completada(self):
        """
        Este método cambia el estado de la tarea a completada.
        """
        self.completada = True

    def __str__(self):
        """
        Este método devuelve una representación en texto de la tarea.
        Puede servir para depuración o para mostrarla como string.
        """
        estado = "[Hecho]" if self.completada else "[Pendiente]"
        return f"{estado} {self.descripcion}"