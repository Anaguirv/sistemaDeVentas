import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_LATERAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_EDITAR_TABLA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from formularios.formulario_info import Formulario_info
from formularios.formulario_salir import Formulario_salir
from formularios.formulario_construccion import FormularioSitioConstruccion
from formularios.formulario_menu import Formulario_menu
from formularios.formulario_config import Formulario_config


class FormularioMaestro(tk.Tk):

    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./imagenes/logo.png", (160,136))
        self.perfil = util_img.leer_imagen("./imagenes/perfil.png", (100, 100))
        self.img_sitio_construccion = util_img.leer_imagen("./imagenes/sitio_construccion.png", (200, 200))
        self.config_window()
        self.paneles()
        self.control_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

    def config_window(self):
        self.title('Sistema de Ventas')
        #self.iconbitmap("./imagenes/icono.ico")
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h) 

    def paneles(self):
         # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_EDITAR_TABLA)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)

    def control_barra_superior(self):
        # Configuracion de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de titulo
        self.labelTitulo = tk.Label(self.barra_superior, text="Donde la Tia")
        self.labelTitulo.config(fg='#fff', font=("Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón menú lateral
        self.botonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                          bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white", relief="solid", command=self.toggle_panel)
        self.botonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de infromación
        self.labelTitulo = tk.Label(self.barra_superior, text="usuario@latia.cl")
        self.labelTitulo.config(fg="#fff", font=("Roboto, 10"), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)

    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
        
        # Imagen de perfil
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Botones del menú lateral
        self.buttonVenta = tk.Button(self.menu_lateral)        
        self.buttonMenu = tk.Button(self.menu_lateral)        
        self.buttonSettings = tk.Button(self.menu_lateral)
        self.buttonInfo = tk.Button(self.menu_lateral)        
        self.buttonSalir = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Venta", "\uf109", self.buttonVenta, self.abrir_panel_construccion),
            ("Menú", "\uf007", self.buttonMenu, self.abrir_panel_menu),
            ("Configuración", "\uf013", self.buttonSettings, self.abrir_panel_config),
            ("Información", "\uf129", self.buttonInfo, self.abrir_panel_info),
            ("Salir", "\uf03e", self.buttonSalir, self.abrir_panel_salir)
        ]

        for text, icon, button, comando in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu, comando)                    
    

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f"  {'-':<5} {text}", anchor="w", font=font_awesome,
                        bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu, command=comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(activebackground=COLOR_MENU_CURSOR_ENCIMA)

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL)

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')
    
    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self.logo,
                            bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def abrir_panel_info(self):
        Formulario_info()

    def abrir_panel_salir(self):
        Formulario_salir(self)

    def abrir_panel_construccion(self):
        self.limpiar_panel(self.cuerpo_principal)     
        FormularioSitioConstruccion(self.cuerpo_principal, self.img_sitio_construccion)

    def abrir_panel_menu(self):
        self.limpiar_panel(self.cuerpo_principal)     
        Formulario_menu(self.cuerpo_principal)

    def abrir_panel_config(self):
        self.limpiar_panel(self.cuerpo_principal)
        Formulario_config(self.cuerpo_principal)



    def limpiar_panel(self,panel):
        # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()
