from tkinter import *
from tkinter import ttk
from tkinter import  messagebox

usuario = ""
contraseña = ""
vUsuarios= []

def guardarDatos(): #EL GET() DEVUELVE LO QUE HAYAS PUESTO
    usuario = datosUsuario.get()
    contraseña = datosContraseña.get()
    contraseña2 = datosContraseña2.get()

    if contraseña==contraseña2:
        vUsuarios.append(usuario)
        vUsuarios.append(contraseña)
        datosUsuario.delete((0), len(usuario))
        datosContraseña.delete((0), len(contraseña))
        datosContraseña2.delete((0), len(contraseña2))
        messagebox.showinfo("Usuario Guardado", f"Usuario {usuario} guardado")
    print(vUsuarios)
    



ventana = Tk()
ventana.title("Datos entrada")
ventana.geometry("430x200")
ventana.resizable(False,False)
ventana.config(background="silver")

#pintar en pantalla

label_Titulo= ttk.Label(ventana, text="DATOS USUARIO")
label_Titulo.config(background="silver", border=2, font=("Times New Roman",20))

label_Usuario= ttk.Label(ventana, text="Usuario:" )
datosUsuario= ttk.Entry(ventana)

label_Contraseña= ttk.Label(ventana, text="Contraseña:" )
datosContraseña= ttk.Entry(ventana, show="*")

label_Contraseña2= ttk.Label(ventana, text="Confirma contraseña:" )
datosContraseña2= ttk.Entry(ventana, show="*")

botonGuardar= ttk.Button(ventana, text="Guardar", command= guardarDatos)
botonSalir = ttk.Button(ventana, text="Salir", command= ventana.destroy)

#Config pantalla

label_Titulo.grid(row=0, column=0, pady=7)

label_Usuario.grid(row=1,column=0, pady=7)
datosUsuario.grid(row=1,column=1, pady=7)
#PADX=15 PARA PONER DISTANCIA EN LA COORDENADA X
#PADY= 15 PARA PONER DISTANCIA EN LA COORDENADA Y
label_Contraseña.grid(row=2,column=0, pady=7)
datosContraseña.grid(row=2,column=1, pady=7)

label_Contraseña2.grid(row=3,column=0, pady=7)
datosContraseña2.grid(row=3,column=1, pady=7)

botonGuardar.grid(row=4,column=0, pady=7)
botonSalir.grid(row=4,column=1, pady=7)


ventana.mainloop()