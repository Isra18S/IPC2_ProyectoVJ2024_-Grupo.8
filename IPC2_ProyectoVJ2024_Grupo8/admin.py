import tkinter as tk
from tkinter import messagebox

def open_new_window():
    def option_selected(option):
        if option != "Cargar":  # Mostrar mensaje solo si se selecciona una opción específica
            messagebox.showinfo("Opción seleccionada", f"Has seleccionado: {option}")

    new_window = tk.Tk()
    new_window.title("Nueva Ventana")
    new_window.geometry("600x300+100+100")  # Ajusta la posición y tamaño de la ventana principal

    label = tk.Label(new_window, text="¡Bienvenido a la nueva ventana!")
    label.pack(pady=20)

    options = ["Usuarios", "Productos", "Empleados", "Actividades"]
    selected_option = tk.StringVar(new_window)
    selected_option.set("Cargar")  # Opción por defecto

    def execute_selected(option):
        option_selected(option)

    def update_menu_label():
        pass  # No hace nada para mantener "Cargar" como está

    # Primer Menubutton y Menu
    menu_button1 = tk.Menubutton(new_window, text="Cargar", indicatoron=True, relief="raised", borderwidth=2)
    menu_button1.place(x=0, y=0)  # Posicionar en la esquina superior izquierda

    menu1 = tk.Menu(menu_button1, tearoff=False)
    menu_button1.config(menu=menu1)

    for item in options:
        menu1.add_command(label=item, command=lambda item=item: execute_selected(item))

    # Segundo Menubutton y Menu (al lado del primero)
    menu_button2 = tk.Menubutton(new_window, text="Cargar", indicatoron=True, relief="raised", borderwidth=2)
    menu_button2.place( x = 50, y=0)  # Alineado junto al primero

    menu2 = tk.Menu(menu_button2, tearoff=False)
    menu_button2.config(menu=menu2)

    for item in options:
        menu2.add_command(label=item, command=lambda item=item: execute_selected(item))

    new_window.mainloop()

