#from graphviz import Digraph
import tkinter as tk
from tkinter import messagebox
#import tkinter

class AppInicio:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("IPC2market")
        ventana.geometry("600x400")

        #img = tkinter.PhotoImage(file="carrito.png")
        #lbl_img = tkinter.Label(ventana, image = img)
        #lbl_img.pack()
        # NO SALE LA IMAGEN 7o7

        self.label_titulo = tk.Label(ventana, text="IPC2market")
        self.label_titulo.pack()

        self.label_user = tk.Label(ventana, text="Usuario")
        self.label_user.pack()
        self.entry_user = tk.Entry(ventana)
        self.entry_user.pack()

        self.label_pass = tk.Label(ventana, text="Contraseña")
        self.label_pass.pack()
        self.entry_pass = tk.Entry(ventana, show="*")
        self.entry_pass.pack()

        self.login_button = tk.Button(ventana, text="Ingresar", command=self.login)
        self.login_button.pack()

    def login(self):
        usuario = self.entry_user.get()
        contraseña = self.entry_pass.get()
        
        if usuario == "AdminIPC2" and contraseña == "IPC2VJ2024":
            messagebox.showinfo("IPC2market", "Aceptado!")
            
        else:
            messagebox.showwarning("IPC2market", "Usuario o contraseña incorrecto!!")

root = tk.Tk()
app = AppInicio(root)
root.mainloop()
