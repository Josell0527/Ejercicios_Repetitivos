from tkinter import *
from tkinter import ttk

#generar la ventana
ventana = Tk()
ventana.title("Primer ejercicio")
ventana.geometry("400x400")
ventana.resizable(width=False,height=False)
ventana.config(background="Turquoise")

#Genera el lienzo para pintar componentes
frm = ttk.Frame(ventana).pack()

#Componentes Label y Button
LabelTexto= ttk.Label(frm, text="Hola Mundo")
LabelTexto.config(background="Ivory", border=2, font=("Times New Roman",15))
LabelTexto.pack()

ttk.Button(frm, text="SALIR", command=ventana.destroy).pack()

ventana.mainloop()