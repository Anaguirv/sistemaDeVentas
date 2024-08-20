import tkinter as tk
import util.util_ventana as util_ventana
from config import COLOR_CUERPO_PRINCIPAL, COLOR_EDITAR_TABLA

class Formulario_info(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.config_window()
        self.construirWidget()

    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Información')
        self.config(bg=COLOR_EDITAR_TABLA)
        self.resizable(0,0)
        w, h,= 400, 150

        util_ventana.centrar_ventana(self, w, h)


    def construirWidget(self):
        self.labelVersion = tk.Label(self, text="Version: 1.0")
        self.labelVersion.config(bg=COLOR_EDITAR_TABLA ,fg="white", font=("Roboto", 15), pady=10, width=20)
        self.labelVersion.pack()
        
        self.labelAutor = tk.Label(self, text="Autor: Arnoldo Aguirre")
        self.labelAutor.config(bg=COLOR_EDITAR_TABLA,fg="white", font=("Roboto", 15), pady=10, width=20)
        self.labelAutor.pack() 

        self.labelMail = tk.Label(self, text="Mail: a.aguirre.dev@gmail.com")
        self.labelMail.config(bg=COLOR_EDITAR_TABLA, fg="white", font=("Roboto", 15), pady=10)
        self.labelMail.pack() 