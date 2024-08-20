from  PIL import Image
from PIL import ImageTk

def leer_imagen(path, size):
    # Trae una imagen y la ajusta al tamaño indicado

    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))