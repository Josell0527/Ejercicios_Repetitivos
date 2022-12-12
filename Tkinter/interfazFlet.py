import flet as ft

# Utilizar flet como ft

def main(page: ft.Page):
    page.title= "APLICACIÓN FLET"
    def cambiarColor(e):
       t.value= textField_Nombre.value
       page.update()

    #Crear texto
    t = ft.Text(value="Introducción a Flet", color= "purple", size=30)

    #Poner en la pantalla el texto
    page.add(t)   #add hace dos cosas: 1-Añadir 2-Actualizar

    t.value="TIENDA PACO"
    page.update() #Refrescar la pantalla para poner un nuevo texto

    #Componente Botón               Generar icono                        Declarar función
    boton= ft.FloatingActionButton(icon=ft.icons.ADD, on_click= cambiarColor)
    page.add(boton)
    
    textField_Nombre= ft.TextField(label="Nombre", hint_text="Escribe tu nombre")
    textField_Nombre
    page.add(textField_Nombre)
    
    dropDown_Menu= ft.Dropdown(width=300, options=[ft.dropdown.Option("Tomate")]) #Opción para elegir
    page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Zanahoria"))
    page.update()
    
    slider_edad= ft.Slider(min=0, max=120, divisions=120, label="Edad: {value}") #Barra de edad
    page.add(slider_edad)
ft.app(target=main)
