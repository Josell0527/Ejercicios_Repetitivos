from tkinter import *
from tkinter import ttk

def guardarDatos():
    print("Guardado")


ventana = Tk()
ventana.title("Datos entrada")
ventana.geometry("430x275")
ventana.resizable(False,False)
ventana.config(background="silver")


alimento = ttk.Combobox(ventana, values=["Carne", "Verdura"], state="readonly")
alimento.place(x=20, y=150)
alimento.set("Elige un alimento")


alimento2 = ttk.Combobox(ventana, values=[""], state="readonly")
alimento2.place(x=200, y=150)
alimento2.set("Opcion")

botonGuardar= ttk.Button(ventana, text="Guardar", command= guardarDatos)
botonGuardar.grid(row=4,column=0, pady=7)

ventana.mainloop()