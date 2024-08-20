import tkinter as tk
import util.util_ventana as util_ventana
from config import COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA

class Formulario_salir(tk.Toplevel):
    def __init__(self, app):
        super().__init__()
        self.app = app 
        self.config_window()
        self.construirWidget()
        self.construirBoton()

    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Salir')
        self.config(bg=COLOR_CUERPO_PRINCIPAL)
        self.resizable(0,0)
        w, h,= 400, 150

        util_ventana.centrar_ventana(self, w, h)    

    def construirWidget(self):
        self.labelVersion = tk.Label(self, text="¿Deseas salir?")
        self.labelVersion.config(bg=COLOR_CUERPO_PRINCIPAL ,fg="black", font=("Roboto", 15), pady=10, width=20)
        self.labelVersion.pack()
    
    def construirBoton(self):
        self.button_no = tk.Button(self, text='No', command=self.destroy)
        self.button_no.config(width=10, font=('Roboto', 12), bg=COLOR_MENU_LATERAL, cursor='hand2', activebackground=COLOR_MENU_CURSOR_ENCIMA)
        self.button_no.pack(side=tk.BOTTOM, anchor=tk.CENTER, padx=10, pady=(0, 10))

        self.button_si = tk.Button(self, text='Si', command=self.cerrar_app)
        self.button_si.config(width=10, font=('Roboto', 12), bg=COLOR_MENU_LATERAL, cursor='hand2', activebackground=COLOR_MENU_CURSOR_ENCIMA)
        self.button_si.pack(side=tk.BOTTOM, anchor=tk.CENTER, padx=10, pady=(0, 10))

    def cerrar_app(self):
        self.app.destroy()
    
