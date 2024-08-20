import tkinter as tk
from tkinter import ttk
from config import  COLOR_EDITAR_TABLA
from model.menu_dao import Menu, guardar, editar, listar, eliminar
from tkinter import messagebox




class Formulario_menu():
    def __init__(self,panel_principal):
        self.id_menu=None
        self.barra_superior(panel_principal)
        self.desabilitar_campos()
        self.tabla_productos(panel_principal)
        self.actualizar_tabla()


# ---------------------------- Funciones---------------------------------------  

    def barra_superior(self, panel_principal):
        # Crear paneles: barra superior
        self.barra_superior = tk.Frame( panel_principal)
        self.barra_superior.config(bg=COLOR_EDITAR_TABLA)
        self.barra_superior.pack(side=tk.TOP, fill=tk.Y, expand=False) 


        # Label de cada campo
        self.label_nombre = tk.Label(self.barra_superior, text='Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'), bg=COLOR_EDITAR_TABLA)
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self.barra_superior, text='Precio: ')
        self.label_duracion.config(font=('Arial', 12, 'bold'), bg=COLOR_EDITAR_TABLA)
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self.barra_superior, text='Categoria: ')
        self.label_genero.config(font=('Arial', 12, 'bold'), bg=COLOR_EDITAR_TABLA)
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        # Entrys de cada campo
        self.mi_nombre = tk.StringVar() # Usar para limpiar campos de entrys
        self.entry_nombre = tk.Entry(self.barra_superior, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.mi_precio = tk.StringVar() # Usar para limpiar campos de entrys
        self.entry_precio = tk.Entry(self.barra_superior, textvariable=self.mi_precio)
        self.entry_precio.config(width=50, font=('Arial', 12))
        self.entry_precio.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.mi_categoria = tk.StringVar() # Usar para limpiar campos entrys
        self.entry_categoria = tk.Entry(self.barra_superior, textvariable=self.mi_categoria)
        self.entry_categoria.config(width=50, font=('Arial', 12))
        self.entry_categoria.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        # Botones
        self.boton_guardar = tk.Button(self.barra_superior, text='Guardar', command=self.guardar_datos)
        self.boton_guardar.config(width=15, font=('Arial', 11,'bold'), fg='#FFFFFF', bg='#0020E7',
                                cursor='hand2', activebackground='#0085E7')
        self.boton_guardar.grid(row=3, column=1, padx=0, pady=15)

        self.boton_cancelar = tk.Button(self.barra_superior, text='Cancelar', command=self.desabilitar_campos)
        self.boton_cancelar.config(width=15, font=('Arial', 11,'bold'), fg='#FFFFFF', bg='#C90000',
                                cursor='hand2', activebackground='#E70000')
        self.boton_cancelar.grid(row=3, column=2, padx=0, pady=15)


    def desabilitar_campos(self):
        # Enviar datos vacios para limpiar campos de entrys
        self.mi_nombre.set('')
        self.mi_precio.set('')
        self.mi_categoria.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_precio.config(state='disabled')
        self.entry_categoria.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')


    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_precio.config(state='normal')
        self.entry_categoria.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')


    def guardar_datos(self):
            
        menu = Menu(
            self.mi_nombre.get(),
            self.mi_precio.get(),
            self.mi_categoria.get()
        )

        if self.id_menu == None:
            guardar(menu)
        else:
            editar(menu, self.id_menu)

        # Actualizar tabla
        self.actualizar_tabla()
        self.desabilitar_campos()


    def editar_datos(self):
        try:
            self.id_menu=self.tabla.item(self.tabla.selection())['text']
            self.nombre_producto=self.tabla.item(
                self.tabla.selection())['values'][0]
            self.precio_producto=self.tabla.item(
                self.tabla.selection())['values'][1]
            self.categoria_producto=self.tabla.item(
                self.tabla.selection())['values'][2]
            
            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_producto)
            self.entry_precio.insert(0, self.precio_producto)
            self.entry_categoria.insert(0, self.categoria_producto)

        except:
            titulo='Edicion de datos'
            mensaje='No ha seleccionado un registro'
            messagebox.showerror(titulo, mensaje)
    

    def eliminar_datos(self):
        try:
            self.id_menu=self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_menu)

            # Actualizar tabla
            self.actualizar_tabla()
            # Reiniciar ID
            self.id_menu = None
        except:
            titulo="Edicion de datos"
            mensaje="No ha seleccionado un registro"
            messagebox.showerror(titulo, mensaje)


    # Cración de la tabla de datos -------------------------------------------------------------
    def tabla_productos(self, panel_principal):

        # Crear paneles: barra superior
        self.tabla_productos = tk.Frame( panel_principal)
        self.tabla_productos.pack(side=tk.TOP, fill=tk.BOTH, expand=False) 

        self.tabla = ttk.Treeview(panel_principal, columns=('Nombre', 'Precio', 'Categoria'))
        self.tabla.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.tabla.column('#0', width=50)   # Ajustar el ancho de la primera columna (ID)
        self.tabla.column('#1', width=150)  # Ajustar el ancho de la segunda columna (Nombre)
        self.tabla.column('#2', width=100)  # Ajustar el ancho de la tercera columna (Precio)
        self.tabla.column('#3', width=100)  # Ajustar el ancho de la cuarta columna (Categoria)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='PRECIO')
        self.tabla.heading('#3', text='CATEGORIA')

        # Scrollbar vertical a la derecha
        self.scroll_vertical = ttk.Scrollbar(self.tabla, orient='vertical', command=self.tabla.yview)
        self.scroll_vertical.pack(side=tk.RIGHT, fill=tk.Y)

        # Asociar la barra de desplazamiento con la tabla
        self.tabla.configure(yscrollcommand=self.scroll_vertical.set)

        # Botones de tabla
        self.boton_nuevo = tk.Button(panel_principal, text='Nuevo', command=self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12,'bold'), fg='#000000', bg='#BEBEBE',
                                cursor='hand2', activebackground='#00E70D')
        self.boton_nuevo.pack(side=tk.TOP, fill=tk.X, expand=False)

        self.boton_editar = tk.Button(panel_principal, text='Editar', command=self.editar_datos)
        self.boton_editar.config(width=10, font=('Arial', 12,'bold'), fg='#000000', bg='#BEBEBE',
                                cursor='hand2', activebackground='#0020E7')
        self.boton_editar.pack(side=tk.TOP, fill=tk.X, expand=False)

        self.boton_eliminar = tk.Button(panel_principal, text='Eliminar', command=self.eliminar_datos)
        self.boton_eliminar.config(width=10, font=('Arial', 12,'bold'), fg='#000000', bg='#BEBEBE',
                                cursor='hand2', activebackground='#E70000')
        self.boton_eliminar.pack(side=tk.TOP, fill=tk.X, expand=False)


    def actualizar_tabla(self):
        # Limpiar la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Recuperar la lista del menú
        self.lista_menu = listar()
        self.lista_menu.reverse()

        # iterar lista de menu para mostrar cada elemento en la tabla
        for p in self.lista_menu:
            self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3]))

