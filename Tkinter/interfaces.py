from tkinter import *
from tkinter import ttk

def saludar():
    texto= campoTexto.get()
    textoLabel.set(texto)

#generar la ventana
ventana = Tk()
ventana.title("Primer ejercicio")
ventana.geometry("400x400")
ventana.resizable(width=False,height=False)
ventana.config(background="Turquoise")

#Genera el lienzo para pintar componentes
frm = ttk.Frame(ventana).pack()

#Componentes Label y Button
textoLabel = StringVar()
textoLabel.set("Hola Tkinter")
LabelTexto= ttk.Label(frm, textvariable=textoLabel)
LabelTexto.config(background="Ivory", border=2, font=("Times New Roman",15))
LabelTexto.pack()

#Componente cuadro de texto
campoTexto= ttk.Entry(frm)
campoTexto.pack()

ttk.Button(frm, text="Saludo", command=saludar).pack()
ttk.Button(frm, text="SALIR", command=ventana.destroy).pack()



ventana.mainloop()
