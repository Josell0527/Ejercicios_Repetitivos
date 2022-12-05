import flet as ft

# Utilizar flet como ft

def main(page: ft.Page):
    page.title= "APLICACIÓN FLET"
    def cambiarColor(e):
       t.value= textField_Nombre.value
       page.update()

    #Crear texto
    t = ft.Text(value="Introducción a Flet", color= "green", size=30)

    #Poner en la pantalla el texto
    page.add(t)   #add hace dos cosas: 1-Añadir 2-Actualizar

    t.value="Hola Paco"
    page.update() #Refrescar la pantalla para poner un nuevo texto

    #Componente Botón               Generar icono                        Declarar función
    boton= ft.FloatingActionButton(icon=ft.icons.ADD, on_click= cambiarColor)
    page.add(boton)
    
    textField_Nombre= ft.TextField(label="Nombre", hint_text="Escribe tu nombre")
    textField_Nombre
    page.add(textField_Nombre)

ft.app(target=main)