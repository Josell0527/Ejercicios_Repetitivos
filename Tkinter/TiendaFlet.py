import flet as ft

# Utilizar flet como ft
compra=[]

def main(page: ft.Page):
    page.title= "Tienda FLET"
    def añadirlista(e):
        compra.append(dropDown_Menu.value)
        t2.value=""
        for i in compra: #Añadir valores a la lista
            t2.value+= i + "\n"
        print(compra)
        page.update()


    #Crear texto
    t = ft.Text(value="Tienda LLavero", color= "Blue", size=30)

    #Poner en la pantalla el texto
    page.add(t)   #add hace dos cosas: 1-Añadir 2-Actualizar
    t.value="FRUTERIA"
    page.update() #Refrescar la pantalla para poner un nuevo texto

    #Componente Botón               Generar icono                        Declarar función
    page.add(ft.FilledButton("Añadir a la cesta", icon="add", on_click= añadirlista))  
    textField_Nombre= ft.TextField(label="Nombre", hint_text="Escribe tu nombre")
    textField_Nombre
    
    dropDown_Menu= ft.Dropdown(width=300, options=[ft.dropdown.Option("Tomate")]) #Opción para elegir
    dropDown_Menu.options.append(ft.dropdown.Option("Zanahoria"))
    page.update()
    
            #Crear fila
    fila= ft.Row(controls=[textField_Nombre, dropDown_Menu])
    page.add(fila)
    
    t3 = ft.Text(value="Elementos añadidos:", color= "black", size=20)
    page.add(t3)
    
    t2 = ft.Text(value="", color= "black", size=20) #Elementos compra
    page.add(t2)
    page.update()
    
    

ft.app(target=main)
