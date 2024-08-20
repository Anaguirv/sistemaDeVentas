from model.conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE menu(
        id_menu INTEGER,
        nombre VARCHAR(100),
        precio INTEGER,
        categoria VARCHAR(100),
        PRIMARY KEY(id_menu AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar
        titulo = 'Crear registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
        
    except:
        titulo = 'Crear registro'
        mensaje = 'La tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)

def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE menu'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar
        titulo = 'Borrar registro'
        mensaje = 'La tabla se borro con éxito'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar registro'
        mensaje = 'No hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)


# -> En patron Modelo-Vista-Presentarior la siguiente sección es analoga a la capa Presentador
        
#Modulo: Menu_DTO
class Menu:
    def __init__(self, nombre, precio, categoria):
        self.id_menu=None
        self.nombre=nombre
        self.precio=precio
        self.categoria=categoria

    def __str__(self):
        return  f"Menu{self.nombre,self.precio, self.categoria}"

# Modulo: Menu_caso.uso
def guardar(menu):
    conexion = ConexionDB()

    sql = f"""INSERT INTO menu (nombre, precio, categoria)
    VALUES('{menu.nombre}','{menu.precio}','{menu.categoria}')"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion al registro'
        mensaje = 'La tabla de menu no esta creado en la base de datos'
        messagebox.showerror(titulo, mensaje)

def listar():
    conexion = ConexionDB()

    lista_menu = []
    sql = 'SELECT * FROM menu'

    try:
        conexion.cursor.execute(sql)
        lista_menu = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la base de datos en la pestaña "Configuración"'
        messagebox.showwarning(titulo, mensaje)
    
    return lista_menu

def editar(menu, id_menu):
    conexion = ConexionDB()

    sql = f"""UPDATE menu
    SET nombre='{menu.nombre}', precio='{menu.precio}',
    categoria='{menu.categoria}'
    WHERE id_menu={id_menu}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'No se puede editar el registro'
        messagebox.showwarning(titulo, mensaje)

def eliminar(id_menu):
    conexion=ConexionDB()
    sql=f'DELETE FROM menu WHERE id_menu = {id_menu}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo="Eliminar Datos"
        mensaje="No se pudo eliminar el registro"
        messagebox.showerror(titulo,mensaje)
