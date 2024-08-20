import tkinter as tk
from config import  COLOR_EDITAR_TABLA
from model.menu_dao import crear_tabla, borrar_tabla


class Formulario_config():
    def __init__(self,panel_principal):
        self.panel_db(panel_principal)



# ---------------------------- Funciones base de datos---------------------------------------  
    def panel_db(self, panel_principal):
        # Crear paneles: Base de datos
        self.barra_db = tk.Frame( panel_principal)
        self.barra_db.config(bg=COLOR_EDITAR_TABLA)
        self.barra_db.pack(side=tk.TOP, fill=tk.X, expand=False) 

        # Label de cada campo
        self.label_db = tk.Label(self.barra_db, text='-   Base de Datos:')
        self.label_db.config(font=('Arial', 12, 'bold'), bg=COLOR_EDITAR_TABLA)
        self.label_db.grid(row=0, column=0, padx=10, pady=10)

        # Botones
        self.boton_nuevo = tk.Button(self.barra_db, text='Crear', command=crear_tabla)
        self.boton_nuevo.config(width=15, font=('Arial', 11,'bold'), fg='#FFFFFF', bg='#00AF0A',
                                cursor='hand2', activebackground='#00E70D')
        self.boton_nuevo.grid(row=0, column=1, padx=10, pady=10)

        self.boton_borrar = tk.Button(self.barra_db, text='Borrar', command=borrar_tabla)
        self.boton_borrar.config(width=15, font=('Arial', 11,'bold'), fg='#FFFFFF', bg='#C90000',
                                cursor='hand2', activebackground='#E70000')
        self.boton_borrar.grid(row=0, column=2, padx=10, pady=10)
