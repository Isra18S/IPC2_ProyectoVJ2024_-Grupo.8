import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from admin import open_new_window

class AppInicio:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("IPC2market")
        ventana.geometry("600x400+500+200")

    # Especifica la ruta de la imagen
        self.image = Image.open("imagenes/carrito.png")
        self.image = self.image.resize((220, 220))
        self.image = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(root, image = self.image)
        self.label.place(x=50, y=60)


        self.label_titulo = tk.Label(ventana, text="IPC2market", font="20")
        self.label_titulo.pack()
        self.label_titulo.place(x=380,y=20)
        
        self.label_user = tk.Label(ventana, text="Usuario")
        self.label_user.pack()
        self.label_user.place(x=400,y=70)
        self.entry_user = tk.Entry(ventana)
        self.entry_user.pack()
        self.entry_user.place(x=365,y=90)

        self.label_pass = tk.Label(ventana, text="Contraseña")
        self.label_pass.pack()
        self.label_pass.place(x=395,y=130)
        self.entry_pass = tk.Entry(ventana, show="*")
        self.entry_pass.pack()
        self.entry_pass.place(x=365,y=150)

        self.login_button = tk.Button(ventana, text="Ingresar", command=self.login)
        self.login_button.pack()
        self.login_button.place(x=400,y=180)

    def login(self):
        usuario = self.entry_user.get()
        contraseña = self.entry_pass.get()
        
        if usuario == "" and contraseña == "":
            self.ventana.destroy()
            open_new_window()
            
        else:
            messagebox.showwarning("IPC2market", "Usuario o contraseña incorrecto!!")

root = tk.Tk()
app = AppInicio(root)
root.mainloop()
