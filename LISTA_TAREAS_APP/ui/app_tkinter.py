import tkinter as tk
from tkinter import ttk, messagebox

from servicios.tarea_servicio import TareaServicio


class AppListaTareas:
    """
    Esta clase corresponde a la capa de interfaz gráfica.
    Aquí se construye la ventana, los widgets y los eventos.

    La lógica de negocio no se implementa aquí directamente,
    sino que se usa la clase TareaServicio.
    """

    def __init__(self, root):
        # Guardamos la ventana principal
        self.root = root

        # Configuración básica de la ventana
        self.root.title("Lista de Tareas")
        self.root.geometry("700x420")
        self.root.resizable(False, False)

        # Creamos una instancia del servicio para manejar la lógica
        self.servicio = TareaServicio()

        # StringVar permite conectar el contenido del Entry con una variable
        self.texto_tarea = tk.StringVar()

        # Creamos los elementos de la interfaz
        self.crear_widgets()

        # Configuramos los eventos extra con bind()
        self.configurar_eventos()

    def crear_widgets(self):
        """
        Este método crea y organiza todos los componentes visuales.
        """

        # Título principal
        titulo = tk.Label(
            self.root,
            text="Aplicación Lista de Tareas",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)

        # Frame superior para la entrada de texto y el botón añadir
        frame_entrada = tk.Frame(self.root)
        frame_entrada.pack(pady=10, padx=10, fill="x")

        # Etiqueta para indicar qué se debe escribir
        lbl_descripcion = tk.Label(frame_entrada, text="Nueva tarea:")
        lbl_descripcion.pack(side="left", padx=(0, 8))

        # Campo de entrada donde el usuario escribe la tarea
        self.entry_tarea = tk.Entry(
            frame_entrada,
            textvariable=self.texto_tarea,
            width=45,
            font=("Arial", 11)
        )
        self.entry_tarea.pack(side="left", padx=(0, 8), fill="x", expand=True)

        # Botón para añadir una nueva tarea
        self.btn_añadir = tk.Button(
            frame_entrada,
            text="Añadir Tarea",
            command=self.agregar_tarea
        )
        self.btn_añadir.pack(side="left")

        # Frame central donde irá la lista de tareas
        frame_lista = tk.Frame(self.root)
        frame_lista.pack(padx=10, pady=10, fill="both", expand=True)

        # Definimos las columnas que tendrá el Treeview
        columnas = ("id", "descripcion", "estado")

        # Creamos el Treeview para mostrar las tareas
        self.tree = ttk.Treeview(
            frame_lista,
            columns=columnas,
            show="headings",
            height=12
        )

        # Encabezados de las columnas
        self.tree.heading("id", text="ID")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.heading("estado", text="Estado")

        # Anchura y alineación de cada columna
        self.tree.column("id", width=60, anchor="center")
        self.tree.column("descripcion", width=430, anchor="w")
        self.tree.column("estado", width=160, anchor="center")

        self.tree.pack(fill="both", expand=True)

        # Configuramos estilos visuales para distinguir tareas pendientes y completadas
        self.tree.tag_configure("completada", foreground="gray")
        self.tree.tag_configure("pendiente", foreground="black")

        # Frame inferior para los botones de acciones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        # Botón para marcar una tarea como completada
        self.btn_completar = tk.Button(
            frame_botones,
            text="Marcar Completada",
            width=18,
            command=self.marcar_completada
        )
        self.btn_completar.pack(side="left", padx=10)

        # Botón para eliminar la tarea seleccionada
        self.btn_eliminar = tk.Button(
            frame_botones,
            text="Eliminar",
            width=18,
            command=self.eliminar_tarea
        )
        self.btn_eliminar.pack(side="left", padx=10)

    def configurar_eventos(self):
        """
        Aquí se configuran los eventos adicionales usando bind().

        - <Return>: al pulsar Enter sobre el campo Entry se añade la tarea.
        - <Double-1>: al hacer doble clic sobre un elemento de la lista
          se marca como completado.
        """

        # Evento de teclado: pulsar Enter en el Entry
        self.entry_tarea.bind("<Return>", self.agregar_tarea_evento)

        # Evento de ratón: doble clic sobre una tarea del Treeview
        self.tree.bind("<Double-1>", self.marcar_completada_evento)

    def agregar_tarea_evento(self, event):
        """
        Este método existe para poder usar bind() con el Entry.

        Cuando un evento se asocia con bind(), Tkinter envía automáticamente
        un parámetro llamado event. Como el método principal agregar_tarea()
        no lo necesita, aquí usamos este método intermedio.
        """
        self.agregar_tarea()

    def marcar_completada_evento(self, event):
        """
        Método intermedio para el evento de doble clic en el Treeview.
        """
        self.marcar_completada()

    def agregar_tarea(self):
        """
        Obtiene el texto escrito por el usuario y pide al servicio
        que cree la tarea.
        Luego actualiza la lista visual.
        """
        try:
            # Recogemos el texto del Entry
            descripcion = self.texto_tarea.get()

            # Delegamos la lógica en la capa de servicios
            self.servicio.agregar_tarea(descripcion)

            # Limpiamos el campo de texto después de añadir
            self.texto_tarea.set("")

            # Refrescamos la lista mostrada en pantalla
            self.actualizar_lista()

            # Devolvemos el foco al Entry para seguir escribiendo cómodamente
            self.entry_tarea.focus()

        except ValueError as e:
            # Mostramos una advertencia si la tarea está vacía
            messagebox.showwarning("Aviso", str(e))

    def obtener_id_seleccionado(self):
        """
        Obtiene el id de la fila seleccionada en el Treeview.

        Devuelve:
        - el id en formato entero si hay selección
        - None si no hay ningún elemento seleccionado
        """
        seleccion = self.tree.selection()

        # Si no hay nada seleccionado, devolvemos None
        if not seleccion:
            return None

        # Tomamos el primer elemento seleccionado
        item = self.tree.item(seleccion[0])

        # values contiene los datos de la fila
        valores = item["values"]

        if not valores:
            return None

        # El primer valor corresponde al id
        return int(valores[0])

    def marcar_completada(self):
        """
        Marca como completada la tarea seleccionada.
        """
        id_tarea = self.obtener_id_seleccionado()

        # Si no se seleccionó ninguna tarea, avisamos al usuario
        if id_tarea is None:
            messagebox.showwarning("Aviso", "Selecciona una tarea primero.")
            return

        try:
            # Usamos el servicio para cambiar el estado de la tarea
            self.servicio.completar_tarea(id_tarea)

            # Actualizamos la lista visual
            self.actualizar_lista()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def eliminar_tarea(self):
        """
        Elimina la tarea seleccionada.
        """
        id_tarea = self.obtener_id_seleccionado()

        # Validamos que el usuario haya seleccionado una tarea
        if id_tarea is None:
            messagebox.showwarning("Aviso", "Selecciona una tarea primero.")
            return

        try:
            # Eliminamos la tarea usando la capa de servicios
            self.servicio.eliminar_tarea(id_tarea)

            # Actualizamos la vista para reflejar el cambio
            self.actualizar_lista()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def actualizar_lista(self):
        """
        Este método vuelve a cargar todas las tareas en el Treeview.

        Primero limpia la tabla y después inserta nuevamente cada tarea
        con su estado actualizado.
        """

        # Borramos todos los elementos actuales del Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertamos otra vez las tareas desde la lista del servicio
        for tarea in self.servicio.listar_tareas():
            # Mostramos un texto diferente según el estado de la tarea
            estado = "Hecho" if tarea.completada else "Pendiente"

            # Copiamos la descripción para poder modificarla visualmente
            descripcion = tarea.descripcion

            # Elegimos la etiqueta visual según el estado
            tag = "completada" if tarea.completada else "pendiente"

            # Si está completada, añadimos un símbolo para dar feedback visual
            if tarea.completada:
                descripcion = f"✔ {descripcion}"

            # Insertamos la fila en el Treeview
            self.tree.insert(
                "",
                "end",
                values=(tarea.id, descripcion, estado),
                tags=(tag,)
            )