import tkinter as tk #Se importa la libreria tkinter para poder usarla y se le pone un alias "tk"
from tkinter import ttk, font  # libreria para dar mas estilos a los elementos
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("800x800")
ventana.config(bg="#424B54")


estilos = ttk.Style(ventana) #darle estilos a los elementos de la ventana)
estilos.theme_use("classic")
estilos.configure ("TFrame", background="#6C7A89", foreground="#102E4A", fieldbackground="#EBF7F7",borderwidth=2, font=("Times New Roman", 12, "bold"))

ventana.columnconfigure(index=0, weight=1)
ventana.rowconfigure(index=0, weight=1)

frame1 = ttk.Frame(ventana)
frame1.columnconfigure(index=0, weight=1)
frame1.columnconfigure(index=1, weight=3)
frame1.rowconfigure(index=0, weight=1)
frame1.rowconfigure(index=1, weight=1)
frame1.rowconfigure(index=2, weight=1)
frame1.rowconfigure(index=3, weight=1)

lbltitulo = ttk.Label(frame1, text="LOGIN")
lbltitulo.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
lbltitulo.configure(font = ("Times New Roman", 14, "bold"))

lblUser = ttk.Label(frame1, text="USERNAME")
lblUser.grid(row=1, column=0, padx=5, pady=5)
lblUser.configure(font = ("Times New Roman", 14, "bold"))

txtUser = ttk.Entry(frame1, font = ("Times New Roman", 14, "bold"))
txtUser.grid(row=1, column=1, padx=5, pady=5)

lblPass = ttk.Label(frame1, text="PASSWORD")
lblPass.grid(row=2, column=0, padx=5, pady=5)

txtPass = ttk.Entry(frame1, font = ("Times New Roman", 14, "bold"), show = "*")
txtPass.grid(row=2, column=1, padx=5, pady=5)

btnIngresar = ttk.Button(frame1,text="INGRESAR")
btnIngresar.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

def ingresar(event): #el event lo que hace es un evento
    usuario = txtUser.get()
    password = txtPass.get()
    if usuario == "usuario" and password == "1234":
        messagebox.showinfo("Ingresar","Ingresado correctamente")
        paginaprincipal()
        ventana.withdraw()
    else:
        messagebox.showinfo("Ingresar","Ingresado incorrecto")
def paginaprincipal():
    ventanaprincipal = tk.Toplevel() #creamos una ventana y aparece hasta que se llame la funcion
    ventanaprincipal.title("Pagina Principal")
    ventanaprincipal.geometry("800x800")
    ventanaprincipal.config(bg="#424B54")
    ventanaprincipal.columnconfigure(index=0, weight=1)

    frame2 = ttk.Frame(ventanaprincipal)
    frame2.columnconfigure(index=0, weight=1)
    frame2.columnconfigure(index=1, weight=30)
    frame2.rowconfigure(index=0, weight=1)
    frame2.rowconfigure(index=1, weight=1)
    frame2.rowconfigure(index=2, weight=1)
    frame2.rowconfigure(index=3, weight=1)

    estilos2 = ttk.Style(ventanaprincipal)
    estilos2.theme_use("clam")
    estilos2.configure("Treeview",background="#424B54",foreground = "#02F5EF",fieldbackground="#424B54",font=("Times New Roman", 12, "bold"),rowheight=40)
    estilos2.map("Treeview", background=[("selected","red")],foreground=[("selected","Blue")])

    lbltext = ttk.Label(frame2,text="El catálogo lo empezamos nosotros, pero lo terminas tú ¡Te damos la bienvenida a nuestro espacio de productos! Aquí vas a encontrar una selección diseñada para hacer tu vida más fácil, cómoda y con estilo. Pero queremos que esta experiencia sea verdaderamente tuya.¿Ves algo que te encanta? Añádelo a tu carrito. ¿Tienes en mente algo genial que no encuentras o quieres vender con nosotros? ¡Tú también puedes agregar tus propios productos a la plataforma! " \
    "Explora, descubre y haz crecer esta comunidad a tu manera.",    wraplength=700,
    justify="left")
    lbltext.grid(ipady=20,row=3, column=0, padx=5, pady=5)
    lbltext.configure(font = ("Times New Roman", 14, "bold"))
    # =========================
    # FUNCIONES DEL MENÚ
    # =========================

    def productos():
        messagebox.showinfo("Productos", "Abrir módulo de Productos")

    def clientes():
        messagebox.showinfo("Clientes", "Abrir módulo de Clientes")

    # =========================
    # BARRA DE MENÚ
    # =========================

    barra_menu = tk.Menu(ventanaprincipal)

    menu_navegacion = tk.Menu(barra_menu, tearoff=0)

    menu_navegacion.add_command(
        label="📦 Productos",
        command=productos
    )

    menu_navegacion.add_command(
        label="👥 Clientes",
        command=clientes
    )

    menu_navegacion.add_separator()

    menu_navegacion.add_command(
        label="❌ Salir",
        command=ventanaprincipal.destroy
    )

    barra_menu.add_cascade(
        label="☰ MENÚ",
        menu=menu_navegacion
    )

    ventanaprincipal.config(menu=barra_menu)

    # =========================
    # FRAME PRINCIPAL
    # =========================

    frame2 = ttk.Frame(ventanaprincipal)
    frame2.columnconfigure(index=0, weight=1)
    frame2.grid(row=0, column=0, sticky="nsew")

    # =========================
    # ESTILOS
    # =========================

    estilos2 = ttk.Style(ventanaprincipal)
    estilos2.theme_use("clam")

    estilos2.configure(
        "Treeview",
        background="#424B54",
        foreground="#02F5EF",
        fieldbackground="#424B54",
        font=("Times New Roman", 12, "bold"),
        rowheight=40
    )

    # =========================
    # TEXTO
    # =========================

    lbltext = ttk.Label(
        frame2,
        text="El catálogo lo empezamos nosotros, pero lo terminas tú. "
             "¡Te damos la bienvenida a nuestro espacio de productos! "
             "Aquí vas a encontrar una selección diseñada para hacer tu vida "
             "más fácil, cómoda y con estilo.\n\n"
             "Explora, descubre y haz crecer esta comunidad a tu manera.",
        wraplength=700,
        justify="left",
        font=("Times New Roman", 14, "bold")
    )

    lbltext.grid(row=0, column=0, padx=20, pady=20)
    frame2.grid(row=0, column=0)

btnIngresar.bind("<Button-1>",ingresar) #llama la funcion cuando le doy click
ventana.bind("<Return>",ingresar) #llama la funcion cuando precione enter

frame1.grid(row=0, column=0)

ventana.mainloop()