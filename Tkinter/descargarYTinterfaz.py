from tkinter import *
from tkinter import ttk

from pytube import YouTube

    
def descargarCancion():
    url= datosEntrada.get()
    youtube= YouTube(url)
    cancion = youtube.streams.get_audio_only
    cancion.download()





#Hacer una ventana
ventana = Tk()
#Poner el título
ventana.title("Descargar música")
#tamaño ventana
ventana.geometry("400x150")
#impedir que se cambie de tamaño
ventana.resizable(False,False)
#fondo de color
ventana.config(background="Red")
#datos de entrada
datosEntrada= ttk.Entry()
#poner el cuadro donde queramos
datosEntrada.place(x=120, y=75)
#Crear boton
boton_Descargar= ttk.Button(ventana, text="Descargar", command= descargarCancion)
boton_Descargar.place(x=160, y=110)
#Crear título
Label_Titulo= ttk.Label(ventana, text="Introduce la URL de la canción")
Label_Titulo.place(x=80, y=30)
#cambiar la letra, color, fuente
Label_Titulo.config(background="Ivory", border=2, font=("Times New Roman",15))

ventana.mainloop()