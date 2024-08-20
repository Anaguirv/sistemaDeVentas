from formularios.formulario_maestro import FormularioMaestro
import os


def main():
    app = FormularioMaestro()
    print(os.getcwd()) #Conocer la ruta 


    app.mainloop()


if __name__=='__main__':
        main()