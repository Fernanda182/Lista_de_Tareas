from modelos.tarea import Tarea


class TareaServicio:
    """
    Esta clase pertenece a la capa de servicios.
    Aquí se concentra la lógica del programa, es decir:
    - agregar tareas
    - listar tareas
    - completar tareas
    - eliminar tareas

    La idea es no mezclar esta lógica con la interfaz gráfica.
    """

    def __init__(self):
        # Lista donde se almacenarán las tareas creadas
        self.tareas = []

        # Contador para generar ids únicos automáticamente
        self.contador_id = 1

    def agregar_tarea(self, descripcion):
        """
        Crea una nueva tarea y la añade a la lista.

        Primero se limpia la descripción con strip() para evitar
        que una cadena con solo espacios sea válida.
        """
        descripcion = descripcion.strip()

        # Validamos que el usuario haya escrito algo
        if not descripcion:
            raise ValueError("La descripción de la tarea no puede estar vacía.")

        # Creamos el objeto Tarea
        nueva_tarea = Tarea(self.contador_id, descripcion)

        # Lo añadimos a la lista
        self.tareas.append(nueva_tarea)

        # Aumentamos el contador para la siguiente tarea
        self.contador_id += 1

        return nueva_tarea

    def listar_tareas(self):
        """
        Devuelve la lista completa de tareas.
        """
        return self.tareas

    def completar_tarea(self, id_tarea):
        """
        Busca una tarea por su id y la marca como completada.
        """
        tarea = self.buscar_por_id(id_tarea)

        if tarea:
            tarea.marcar_completada()
            return tarea

        # Si no existe una tarea con ese id, se lanza un error
        raise ValueError("No se encontró la tarea seleccionada.")

    def eliminar_tarea(self, id_tarea):
        """
        Busca una tarea por su id y la elimina de la lista.
        """
        tarea = self.buscar_por_id(id_tarea)

        if tarea:
            self.tareas.remove(tarea)
            return tarea

        # Si no existe una tarea con ese id, se lanza un error
        raise ValueError("No se encontró la tarea seleccionada.")

    def buscar_por_id(self, id_tarea):
        """
        Recorre la lista de tareas y devuelve la tarea
        cuyo id coincida con el recibido.
        """
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                return tarea

        # Si no se encuentra, devolvemos None
        return None