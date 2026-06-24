import tkinter as tk #Se importa la libreria tkinter para poder usarla y se le pone un alias "tk"
from tkinter import ttk, font  # libreria para dar mas estilos a los elementos
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("800x800")
ventana.config(bg="#DDECED")


estilos = ttk.Style(ventana) #darle estilos a los elementos de la ventana)
estilos.theme_use("classic")
estilos.configure(ventana, background="#DDECED", foreground="#02F5EF", fieldbackground="#EBF7F7")

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
lbltitulo.configure(font = ("New York Times", 14, "bold"))

lblUser = ttk.Label(frame1, text="USERNAME")
lblUser.grid(row=1, column=0, padx=5, pady=5)
lblUser.configure(font = ("New York Times", 14, "bold"))

txtUser = ttk.Entry(frame1, font = ("New York Times", 14, "bold"))
txtUser.configure(font = ("New York Times", 14, "bold"))
txtUser.grid(row=1, column=1, padx=5, pady=5)

lblPass = ttk.Label(frame1, text="PASSWORD")
lblPass.configure(font = ("New York Times", 14, "bold"))
lblPass.grid(row=2, column=0, padx=5, pady=5)

txtPass = ttk.Entry(frame1, font = ("New York Times", 14, "bold"))
txtPass.configure(font = ("New York Times", 14, "bold"), show = "*")
txtPass.grid(row=2, column=1, padx=5, pady=5)

btnIngresar = ttk.Button(frame1,text="INGRESAR", command="")
btnIngresar.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

def ingresar(event): #el event lo que hace
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
    ventanaprincipal.config(bg="#E5C7F2")
    ventanaprincipal.columnconfigure(index=0, weight=1)

    estilos2 = ttk.Style(ventana)
    estilos2.theme_use("clam")
    estilos2.configure("Treeview",background="#E8A9D0",foreground = "#E6279C",fieldbackground="#E8A9D0",font=("New York Times", 12, "bold"),rowheight=40)
    estilos2.map("Treeview", background=[("selected","red")],foreground=[("selected","Blue")])

btnIngresar.bind("<Button-1>",ingresar) #llama la funcion cuando le doy click
btnIngresar.bind("<Return>",ingresar) #llama la funcion cuando precione enter

frame1.grid(row=0, column=0)

ventana.mainloop()