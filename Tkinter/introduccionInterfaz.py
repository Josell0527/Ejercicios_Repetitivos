from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Datos entrada")
ventana.geometry("500x300")
ventana.resizable(False,False)
ventana.config(background="silver")

#pintar en pantalla

label_Titulo= ttk.Label(ventana, text="LLAVERESION")
label_Titulo.config(background="silver", border=2, font=("Times New Roman",20))

label_Usuario= ttk.Label(ventana, text="Usuario:" )
datosUsuario= ttk.Entry(ventana)

label_Contraseña= ttk.Label(ventana, text="Contraseña:" )
datosContraseña= ttk.Entry(ventana)

label_Contraseña2= ttk.Label(ventana, text="Confirma contraseña" )
datosContraseña2= ttk.Entry(ventana)

botonGuardar= ttk.Button(ventana, text="Guardar")


#Config pantalla

label_Titulo.grid(row=0, column=0)

label_Usuario.grid(row=1,column=0)
datosUsuario.grid(row=1,column=1)

label_Contraseña.grid(row=2,column=0)
datosContraseña.grid(row=2,column=1)

label_Contraseña2.grid(row=3,column=0)
datosContraseña2.grid(row=3,column=1)

botonGuardar.grid(row=4,column=0)
#datosUsuario.grid(row=4,column=1)


ventana.mainloop()