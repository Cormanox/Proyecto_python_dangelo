import tkinter as tk # Importamos tkinter para la interfaz gráfica y lo llamamos tk
from tkinter import ttk, messagebox

# Definimos la ventana para el inicio de sesión
ventana = tk.Tk()
ventana.title("Login - Plataforma")
ventana.config(bg="#424B54")

# Calculamos las coordenadas para centrar la ventana de login en el monitor
width = 450
height = 300
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
ventana.geometry('%dx%d+%d+%d' % (width, height, x, y))
ventana.resizable(False, False)

# Configuramos el diseño visual del login con el tema clam
estilos = ttk.Style(ventana)
estilos.theme_use("clam")
estilos.configure("TFrame", background="#6C7A89")
estilos.configure("TLabel", background="#6C7A89", foreground="#ffffff", font=("Times New Roman", 12, "bold"))
estilos.configure("LoginTitle.TLabel", background="#6C7A89", foreground="#02F5EF", font=("Times New Roman", 16, "bold"))
estilos.configure("TButton", font=("Times New Roman", 11, "bold"), background="#102E4A", foreground="#ffffff")
estilos.map("TButton", background=[("active", "#1f4a75")])

ventana.columnconfigure(index=0, weight=1)
ventana.rowconfigure(index=0, weight=1)

frame1 = ttk.Frame(ventana, padding=25)
frame1.columnconfigure(index=0, weight=1)
frame1.columnconfigure(index=1, weight=3)

lbltitulo = ttk.Label(frame1, text="LOGIN DE USUARIO", style="LoginTitle.TLabel")
lbltitulo.grid(row=0, column=0, padx=5, pady=(0, 20), columnspan=2)

lblUser = ttk.Label(frame1, text="USUARIO:", style="TLabel")
lblUser.grid(row=1, column=0, padx=5, pady=8, sticky="w")

txtUser = ttk.Entry(frame1, font=("Times New Roman", 12))
txtUser.grid(row=1, column=1, padx=5, pady=8, sticky="ew")

lblPass = ttk.Label(frame1, text="CONTRASEÑA:", style="TLabel")
lblPass.grid(row=2, column=0, padx=5, pady=8, sticky="w")

txtPass = ttk.Entry(frame1, font=("Times New Roman", 12), show="*")
txtPass.grid(row=2, column=1, padx=5, pady=8, sticky="ew")

def ingresar(event=None):
    usuario = txtUser.get().strip()
    password = txtPass.get().strip()
    if usuario == "usuario" and password == "1234":
        messagebox.showinfo("Ingresar", "¡Ingreso correcto!")
        paginaprincipal()
        ventana.withdraw()
    else:
        messagebox.showwarning("Ingresar", "Credenciales incorrectas")

btnIngresar = ttk.Button(frame1, text="INGRESAR", command=ingresar)
btnIngresar.grid(row=3, column=0, padx=5, pady=(20, 0), columnspan=2, sticky="ew")


def paginaprincipal():
    ventanaprincipal = tk.Toplevel()
    ventanaprincipal.title("Página Principal - Plataforma")
    ventanaprincipal.geometry("850x500")
    ventanaprincipal.config(bg="#424B54")

    # Centramos la ventana principal en pantalla
    p_width = 850
    p_height = 500
    p_x = (screen_width / 2) - (p_width / 2)
    p_y = (screen_height / 2) - (p_height / 2)
    ventanaprincipal.geometry('%dx%d+%d+%d' % (p_width, p_height, p_x, p_y))

    # Definimos la apariencia general de esta ventana principal
    estilos2 = ttk.Style(ventanaprincipal)
    estilos2.theme_use("clam")
    
    # Estilos para los marcos y textos de la ventana principal
    estilos2.configure("Main.TFrame", background="#6C7A89")
    estilos2.configure("Main.TLabel", background="#6C7A89", foreground="#ffffff", font=("Times New Roman", 12, "bold"))
    estilos2.configure("Title.TLabel", background="#6C7A89", foreground="#02F5EF", font=("Times New Roman", 18, "bold"))

    # Estilos específicos para la sección donde se gestionan productos
    estilos2.configure("Prod.TFrame", background="#6C7A89")
    estilos2.configure("Prod.TLabel", background="#6C7A89", foreground="#ffffff", font=("Times New Roman", 11, "bold"))
    estilos2.configure("ProdTitle.TLabel", background="#6C7A89", foreground="#02F5EF", font=("Times New Roman", 13, "bold"))

    # Estilo general para todos los botones de la aplicación
    estilos2.configure("TButton", font=("Times New Roman", 11, "bold"), background="#102E4A", foreground="#ffffff")
    estilos2.map("TButton", background=[("active", "#1f4a75")])

    # Acciones que se ejecutan desde el menú de navegación
    def productos():
        # Ventana para agregar, editar y eliminar productos
        ventanaproduc = tk.Toplevel(ventanaprincipal)
        ventanaproduc.title("Gestión de Productos")
        ventanaproduc.geometry("1000x600")
        ventanaproduc.config(bg="#424B54")

        # Centramos la ventana de productos en la pantalla
        prod_width = 1000
        prod_height = 600
        prod_x = (screen_width / 2) - (prod_width / 2)
        prod_y = (screen_height / 2) - (prod_height / 2)
        ventanaproduc.geometry('%dx%d+%d+%d' % (prod_width, prod_height, prod_x, prod_y))

        # Organizamos la pantalla: formulario a la izquierda y listado a la derecha
        left = ttk.Frame(ventanaproduc, style="Prod.TFrame", padding=15)
        left.pack(side="left", fill="y", padx=15, pady=15)
        right = ttk.Frame(ventanaproduc, style="Prod.TFrame", padding=15)
        right.pack(side="right", fill="both", expand=True, padx=15, pady=15)

        # Título principal del formulario de artículos
        lbl_form_title = ttk.Label(left, text="DATOS DEL ARTÍCULO", style="ProdTitle.TLabel")
        lbl_form_title.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        # Definición de etiquetas y campos de entrada de datos
        ttk.Label(left, text="Código de Producto:", style="Prod.TLabel").grid(row=1, column=0, sticky="w", pady=6)
        ent_codigo = ttk.Entry(left, width=25, font=("Times New Roman", 10))
        ent_codigo.grid(row=1, column=1, pady=6, padx=5)

        ttk.Label(left, text="Nombre del Producto:", style="Prod.TLabel").grid(row=2, column=0, sticky="w", pady=6)
        ent_nombre = ttk.Entry(left, width=25, font=("Times New Roman", 10))
        ent_nombre.grid(row=2, column=1, pady=6, padx=5)

        ttk.Label(left, text="Categoría:", style="Prod.TLabel").grid(row=3, column=0, sticky="w", pady=6)
        cmb_categoria = ttk.Combobox(left, values=("Electrónica", "Ropa", "Hogar", "Alimentos", "Deportes", "Otros"), state="readonly", width=22, font=("Times New Roman", 10))
        cmb_categoria.grid(row=3, column=1, pady=6, padx=5)

        ttk.Label(left, text="Precio (₡):", style="Prod.TLabel").grid(row=4, column=0, sticky="w", pady=6)
        ent_precio = ttk.Entry(left, width=25, font=("Times New Roman", 10))
        ent_precio.grid(row=4, column=1, pady=6, padx=5)

        ttk.Label(left, text="Cantidad / Stock:", style="Prod.TLabel").grid(row=5, column=0, sticky="w", pady=6)
        ent_stock = ttk.Entry(left, width=25, font=("Times New Roman", 10))
        ent_stock.grid(row=5, column=1, pady=6, padx=5)

        ttk.Label(left, text="Estado:", style="Prod.TLabel").grid(row=6, column=0, sticky="w", pady=6)
        cmb_estado = ttk.Combobox(left, values=("Disponible", "Agotado"), state="readonly", width=22, font=("Times New Roman", 10))
        cmb_estado.grid(row=6, column=1, pady=6, padx=5)

        # Botones para gestionar las operaciones del formulario
        btn_agregar = ttk.Button(left, text="Agregar Producto")
        btn_eliminar = ttk.Button(left, text="Eliminar Producto")
        btn_limpiar = ttk.Button(left, text="Limpiar Formulario")

        btn_agregar.grid(row=7, column=0, columnspan=2, pady=(15, 5), sticky="ew")
        btn_eliminar.grid(row=8, column=0, columnspan=2, pady=5, sticky="ew")
        btn_limpiar.grid(row=9, column=0, columnspan=2, pady=5, sticky="ew")

        # Encabezado del área del catálogo
        lbl_table_title = ttk.Label(right, text="CATÁLOGO DE PRODUCTOS REGISTRADOS", style="ProdTitle.TLabel")
        lbl_table_title.pack(anchor="w", pady=(0, 10))

        # Personalización visual de la tabla de productos
        estilos_tree = ttk.Style(ventanaproduc)
        estilos_tree.configure("Prod.Treeview", background="#424B54", foreground="#02F5EF", fieldbackground="#424B54", font=("Times New Roman", 10, "bold"), rowheight=30)
        estilos_tree.map("Prod.Treeview", background=[("selected", "red")], foreground=[("selected", "blue")])

        # Definimos y estructuramos las columnas de la tabla
        cols = ("Código", "Nombre", "Categoría", "Precio", "Stock", "Estado")
        tree = ttk.Treeview(right, columns=cols, show="headings", style="Prod.Treeview")
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, anchor="center", width=110)

        # Barra de desplazamiento vertical para navegar la tabla fácilmente
        scrollbar = ttk.Scrollbar(right, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tree.pack(fill="both", expand=True)

        # Panel inferior para mostrar notificaciones rápidas de estado
        status = ttk.Label(ventanaproduc, text="Total productos: 0", relief="sunken", anchor="w", font=("Times New Roman", 10, "bold"))
        status.pack(side="bottom", fill="x")

        # Función para refrescar el conteo de artículos en la barra inferior
        def actualizar_status():
            total = len(tree.get_children())
            status.config(text=f" Total productos: {total}")

        # Limpia todas las entradas de texto del formulario
        def limpiar_form():
            ent_codigo.delete(0, "end")
            ent_nombre.delete(0, "end")
            cmb_categoria.set("")
            ent_precio.delete(0, "end")
            ent_stock.delete(0, "end")
            cmb_estado.set("")

        # Comprueba que la información ingresada sea correcta antes de registrar el producto
        def validar_y_agregar():
            codigo = ent_codigo.get().strip()
            nombre = ent_nombre.get().strip()
            categoria = cmb_categoria.get().strip()
            precio = ent_precio.get().strip()
            stock = ent_stock.get().strip()
            estado = cmb_estado.get().strip()

            if not (codigo and nombre and categoria and precio and stock and estado):
                messagebox.showwarning("Datos incompletos", "Complete todos los campos antes de agregar el producto.")
                return

            if not codigo.isdigit():
                messagebox.showwarning("Código inválido", "El código del producto debe ser puramente numérico.")
                return

            # Comparamos el código ingresado para asegurarnos de que no esté repetido en la tabla
            for item in tree.get_children():
                val = tree.item(item, "values")
                if val[0] == codigo:
                    messagebox.showwarning("Código duplicado", f"El código '{codigo}' ya está asignado a otro producto.")
                    return

            try:
                precio_f = float(precio)
                if precio_f <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showwarning("Precio inválido", "El precio debe ser un número decimal mayor a 0.")
                return

            try:
                stock_i = int(stock)
                if stock_i < 0:
                    raise ValueError
            except ValueError:
                messagebox.showwarning("Stock inválido", "La cantidad en stock debe ser un número entero mayor o igual a 0.")
                return

            tree.insert("", "end", values=(codigo, nombre, categoria, f"₡{precio_f:.2f}", str(stock_i), estado))
            limpiar_form()
            actualizar_status()

        # Quita de la lista el artículo que el usuario haya marcado
        def eliminar_seleccion():
            sel = tree.selection()
            if not sel:
                messagebox.showinfo("Eliminar", "Seleccione al menos un producto para eliminar.")
                return
            if messagebox.askyesno("Confirmar", "¿Eliminar los productos seleccionados?"):
                for item in sel:
                    tree.delete(item)
                limpiar_form()
                actualizar_status()

        # Rellena el formulario con los detalles del artículo que toquemos en la tabla
        def cargar_desde_tabla(event=None):
            sel = tree.selection()
            if not sel:
                return
            vals = tree.item(sel[0], "values")
            limpiar_form()
            ent_codigo.insert(0, vals[0])
            ent_nombre.insert(0, vals[1])
            cmb_categoria.set(vals[2])

            precio_val = vals[3]
            if precio_val.startswith("₡"):
                precio_val = precio_val[1:]
            ent_precio.insert(0, precio_val)

            ent_stock.insert(0, vals[4])
            cmb_estado.set(vals[5])

        # Conectamos cada botón de la interfaz con su respectiva función
        btn_agregar.config(command=validar_y_agregar)
        btn_eliminar.config(command=eliminar_seleccion)
        btn_limpiar.config(command=limpiar_form)

        # Hacemos que la tabla responda cuando se selecciona una fila
        tree.bind("<<TreeviewSelect>>", cargar_desde_tabla)

        # Insertamos algunos artículos iniciales para que la tabla no se vea vacía
        datos_ejemplo = [
            ("101", "Laptop HP", "Electrónica", 850.00, 15, "Disponible"),
            ("102", "Tenis Deportivos", "Deportes", 75.50, 30, "Disponible"),
            ("103", "Cafetera Oster", "Hogar", 45.00, 0, "Agotado")
        ]
        for cod, nom, cat, pre, st, est in datos_ejemplo:
            tree.insert("", "end", values=(cod, nom, cat, f"₡{pre:.2f}", str(st), est))

        actualizar_status()

    def clientes():
        # Ventana para agregar, editar y eliminar clientes
        ventanaclientes = tk.Toplevel(ventanaprincipal)
        ventanaclientes.title("Gestión de Clientes")
        ventanaclientes.geometry("1000x600")
        ventanaclientes.config(bg="#424B54")

        # Centramos la ventana de clientes en la pantalla
        clie_width = 1000
        clie_height = 600
        clie_x = (screen_width / 2) - (clie_width / 2)
        clie_y = (screen_height / 2) - (clie_height / 2)
        ventanaclientes.geometry('%dx%d+%d+%d' % (clie_width, clie_height, clie_x, clie_y))

        # Configuramos los estilos específicos para esta sección de clientes
        estilos2.configure("Clie.TFrame", background="#6C7A89")
        estilos2.configure("Clie.TLabel", background="#6C7A89", foreground="#ffffff", font=("Times New Roman", 11, "bold"))
        estilos2.configure("ClieTitle.TLabel", background="#6C7A89", foreground="#02F5EF", font=("Times New Roman", 13, "bold"))

        # Estructuramos el diseño: formulario a la izquierda y listado a la derecha
        left = ttk.Frame(ventanaclientes, style="Clie.TFrame", padding=15)
        left.pack(side="left", fill="y", padx=15, pady=15)
        right = ttk.Frame(ventanaclientes, style="Clie.TFrame", padding=15)
        right.pack(side="right", fill="both", expand=True, padx=15, pady=15)

        # Título para la sección del formulario de clientes
        lbl_form_title = ttk.Label(left, text="DATOS DEL CLIENTE", style="ClieTitle.TLabel")
        lbl_form_title.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        # Definición de etiquetas y cajas de texto del formulario
        ttk.Label(left, text="Identificación / Cédula:", style="Clie.TLabel").grid(row=1, column=0, sticky="w", pady=6)
        ent_id = ttk.Entry(left, width=25, font=("Times New Roman", 10))
        ent_id.grid(row=1, column=1, pady=6, padx=5)

        ttk.Label(left, text="Nombre Completo:", style="Clie.TLabel").grid(row=2, column=0, sticky="w", pady=6)
        ent_nombre = ttk.Entry(left, width=25, font=("Times New Roman", 10))
        ent_nombre.grid(row=2, column=1, pady=6, padx=5)

        ttk.Label(left, text="Correo Electrónico:", style="Clie.TLabel").grid(row=3, column=0, sticky="w", pady=6)
        ent_correo = ttk.Entry(left, width=25, font=("Times New Roman", 10))
        ent_correo.grid(row=3, column=1, pady=6, padx=5)

        ttk.Label(left, text="Teléfono:", style="Clie.TLabel").grid(row=4, column=0, sticky="w", pady=6)
        ent_telefono = ttk.Entry(left, width=25, font=("Times New Roman", 10))
        ent_telefono.grid(row=4, column=1, pady=6, padx=5)

        ttk.Label(left, text="Tipo de Cliente:", style="Clie.TLabel").grid(row=5, column=0, sticky="w", pady=6)
        cmb_tipo = ttk.Combobox(left, values=("Regular", "VIP", "Mayorista"), state="readonly", width=22, font=("Times New Roman", 10))
        cmb_tipo.grid(row=5, column=1, pady=6, padx=5)

        ttk.Label(left, text="Estado:", style="Clie.TLabel").grid(row=6, column=0, sticky="w", pady=6)
        cmb_estado = ttk.Combobox(left, values=("Activo", "Inactivo"), state="readonly", width=22, font=("Times New Roman", 10))
        cmb_estado.grid(row=6, column=1, pady=6, padx=5)

        # Botones para ejecutar acciones en el formulario
        btn_agregar = ttk.Button(left, text="Agregar Cliente")
        btn_eliminar = ttk.Button(left, text="Eliminar Cliente")
        btn_limpiar = ttk.Button(left, text="Limpiar Formulario")

        btn_agregar.grid(row=7, column=0, columnspan=2, pady=(15, 5), sticky="ew")
        btn_eliminar.grid(row=8, column=0, columnspan=2, pady=5, sticky="ew")
        btn_limpiar.grid(row=9, column=0, columnspan=2, pady=5, sticky="ew")

        # Título de la tabla de listado de clientes
        lbl_table_title = ttk.Label(right, text="LISTADO DE CLIENTES REGISTRADOS", style="ClieTitle.TLabel")
        lbl_table_title.pack(anchor="w", pady=(0, 10))

        # Personalización de la apariencia para el listado de clientes
        estilos_tree = ttk.Style(ventanaclientes)
        estilos_tree.configure("Clie.Treeview", background="#424B54", foreground="#02F5EF", fieldbackground="#424B54", font=("Times New Roman", 10, "bold"), rowheight=30)
        estilos_tree.map("Clie.Treeview", background=[("selected", "red")], foreground=[("selected", "blue")])

        # Creamos y rotulamos las columnas de la tabla de clientes
        cols = ("Identificación", "Nombre Completo", "Correo", "Teléfono", "Tipo", "Estado")
        tree = ttk.Treeview(right, columns=cols, show="headings", style="Clie.Treeview")
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, anchor="center", width=110)

        # Colocamos una barra de desplazamiento vertical en la tabla
        scrollbar = ttk.Scrollbar(right, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tree.pack(fill="both", expand=True)

        # Franja en la parte inferior para mostrar el número total de clientes
        status = ttk.Label(ventanaclientes, text="Total clientes: 0", relief="sunken", anchor="w", font=("Times New Roman", 10, "bold"))
        status.pack(side="bottom", fill="x")

        # Función para refrescar el total de clientes registrados
        def actualizar_status():
            total = len(tree.get_children())
            status.config(text=f" Total clientes: {total}")

        # Borra el contenido de los campos de texto
        def limpiar_form():
            ent_id.delete(0, "end")
            ent_nombre.delete(0, "end")
            ent_correo.delete(0, "end")
            ent_telefono.delete(0, "end")
            cmb_tipo.set("")
            cmb_estado.set("")

        # Realiza las validaciones de campos antes de meter el cliente a la lista
        def validar_y_agregar():
            ident = ent_id.get().strip()
            nombre = ent_nombre.get().strip()
            correo = ent_correo.get().strip()
            telefono = ent_telefono.get().strip()
            tipo = cmb_tipo.get().strip()
            estado = cmb_estado.get().strip()

            if not (ident and nombre and correo and telefono and tipo and estado):
                messagebox.showwarning("Datos incompletos", "Complete todos los campos antes de agregar el cliente.")
                return

            if not ident.isdigit():
                messagebox.showwarning("Identificación inválida", "La identificación debe contener únicamente números.")
                return

            # Nos aseguramos de que no haya otro cliente con la misma identificación
            for item in tree.get_children():
                val = tree.item(item, "values")
                if val[0] == ident:
                    messagebox.showwarning("ID duplicada", f"La identificación '{ident}' ya está asignada a otro cliente.")
                    return

            # Validamos de manera básica que la dirección de correo tenga @ y un punto
            if "@" not in correo or "." not in correo:
                messagebox.showwarning("Correo inválido", "Ingrese una dirección de correo electrónico válida (debe contener '@' y '.').")
                return

            tree.insert("", "end", values=(ident, nombre, correo, telefono, tipo, estado))
            limpiar_form()
            actualizar_status()

        # Quita de la lista al cliente seleccionado tras pedir confirmación
        def eliminar_seleccion():
            sel = tree.selection()
            if not sel:
                messagebox.showinfo("Eliminar", "Seleccione al menos un cliente para eliminar.")
                return
            if messagebox.askyesno("Confirmar", "¿Eliminar los clientes seleccionados?"):
                for item in sel:
                    tree.delete(item)
                limpiar_form()
                actualizar_status()

        # Rellena el formulario con los detalles del cliente que seleccionemos en la tabla
        def cargar_desde_tabla(event=None):
            sel = tree.selection()
            if not sel:
                return
            vals = tree.item(sel[0], "values")
            limpiar_form()
            ent_id.insert(0, vals[0])
            ent_nombre.insert(0, vals[1])
            ent_correo.insert(0, vals[2])
            ent_telefono.insert(0, vals[3])
            cmb_tipo.set(vals[4])
            cmb_estado.set(vals[5])

        # Conectamos cada botón de la interfaz con su respectiva función
        btn_agregar.config(command=validar_y_agregar)
        btn_eliminar.config(command=eliminar_seleccion)
        btn_limpiar.config(command=limpiar_form)

        # Hacemos que la tabla responda cuando se selecciona una fila
        tree.bind("<<TreeviewSelect>>", cargar_desde_tabla)

        # Insertamos algunos clientes iniciales para pruebas
        datos_ejemplo = [
            ("1001", "Juan Pérez", "juan.perez@email.com", "555-0199", "VIP", "Activo"),
            ("1002", "María López", "maria.lopez@email.com", "555-0245", "Regular", "Activo"),
            ("1003", "Carlos Gómez", "carlos.gomez@email.com", "555-0321", "Mayorista", "Inactivo")
        ]
        for ident, nom, corr, tel, tip, est in datos_ejemplo:
            tree.insert("", "end", values=(ident, nom, corr, tel, tip, est))

        actualizar_status()

    # Configuración de la barra de menú superior
    barra_menu = tk.Menu(ventanaprincipal)

    menu_navegacion = tk.Menu(barra_menu, tearoff=0)

    menu_navegacion.add_command(
        label="Productos",
        command=productos
    )

    menu_navegacion.add_command(
        label="Clientes",
        command=clientes
    )

    menu_navegacion.add_separator()

    menu_navegacion.add_command(
        label="Salir",
        command=ventanaprincipal.destroy
    )

    barra_menu.add_cascade(
        label="MENÚ",
        menu=menu_navegacion
    )

    ventanaprincipal.config(menu=barra_menu)

    # Definimos el marco principal que contiene el mensaje de bienvenida
    frame2 = ttk.Frame(ventanaprincipal, style="Main.TFrame", padding=30)
    frame2.pack(fill="both", expand=True, padx=40, pady=40)

    # Sección del mensaje de bienvenida al usuario
    lbl_bienvenida = ttk.Label(frame2, text="BIENVENIDO A NUESTRO ESPACIO", style="Title.TLabel")
    lbl_bienvenida.pack(pady=(0, 20))

    lbltext = ttk.Label(
        frame2,
        text="El catálogo lo empezamos nosotros, pero lo terminas tú.\n\n"
             "Te damos la bienvenida a nuestro espacio de productos! "
             "Aquí vas a encontrar una selección diseñada para hacer tu vida "
             "más fácil, cómoda y con estilo.\n\n"
             "Explora, descubre y haz crecer esta comunidad a tu manera.",
        wraplength=650,
        justify="center",
        style="Main.TLabel"
    )
    lbltext.pack(fill="both", expand=True)


# Asignamos la tecla Enter para facilitar el inicio de sesión
ventana.bind("<Return>", ingresar)

frame1.grid(row=0, column=0)

ventana.mainloop()