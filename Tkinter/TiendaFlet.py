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

    page.add(
        ft.Stack(
            [
                ft.CircleAvatar(
                    foreground_image_url="https://www.cdc.gov/foodsafety/images/comms/features/GettyImages-1247930626-500px.jpg?_=00453"
                ),
                ft.Container(
                    content=ft.CircleAvatar(bgcolor=ft.colors.GREEN, radius=5),
                    alignment=ft.alignment.bottom_left,
                ),
            ],
            width=40,
            height=40,
        )
    )

    #Crear texto
    t = ft.Text(value="Tienda LLavero", color= "orange", size=30)

    #Poner en la pantalla el texto
    page.add(t)   #add hace dos cosas: 1-Añadir 2-Actualizar
    t.value="FRUTERIA"
    page.update() #Refrescar la pantalla para poner un nuevo texto

    #Componente Botón               Generar icono                        Declarar función
    botoncesta= ft.FilledButton("Añadir a la cesta", icon="add", on_click= añadirlista)  
    textField_Nombre= ft.TextField(label="Nombre", hint_text="Escribe tu nombre")
    textField_Nombre
    
    #Boton añadido correctamente

    def añadido(e):
        page.banner.open= False
        page.snack_bar = ft.SnackBar(ft.Text("Compra realizada correctamente"))
        page.snack_bar.open = True
        page.update()


        #Boton finalizar
    def close_banner(e):
        page.banner.open = False
        page.update()


    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.ADD_SHOPPING_CART_SHARP, color=ft.colors.AMBER, size=40),
        content=ft.Text(f"{textField_Nombre} has seleccionado {compra}"
        ),
        actions=[
            ft.TextButton("Finalizar", on_click=añadido),
            ft.TextButton("Continuar comprando", on_click=close_banner),
        ],
    )
    def show_banner_click(e):
        page.banner.open = True
        page.banner.content= ft.Text(f"{textField_Nombre.value} has seleccionado {compra}")
        dlg_modal.open = False
        page.update()
        
    #Componente Boton Comprado
    def close_dlg(e):
            dlg_modal.open = False
            page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Finalizar compra"),
        content=ft.Text("¿Deseas transmitrar la compra?"),
        actions=[
            ft.TextButton("Si", on_click=show_banner_click),
            ft.TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()


    botonfinalizarcompra= ft.ElevatedButton("Finalizar compra", on_click=open_dlg_modal)

    dropDown_Menu= ft.Dropdown(width=300, options=[ft.dropdown.Option("Tomate")]) #Opción para elegir
    dropDown_Menu.options.append(ft.dropdown.Option("Zanahoria"))
    dropDown_Menu.options.append(ft.dropdown.Option("Pimiento verde"))
    dropDown_Menu.options.append(ft.dropdown.Option("Cebolla"))
    dropDown_Menu.options.append(ft.dropdown.Option("Alcachofas"))
    page.update()

    
            #Crear fila
    fila= ft.Row(controls=[textField_Nombre, dropDown_Menu, ])
    page.add(fila)
    
    fila2= ft.Row(controls=[botoncesta, botonfinalizarcompra])
    page.add(fila2)
    
    t3 = ft.Text(value="Elementos añadidos:", color= "black", size=20)
    page.add(t3)
    
    t2 = ft.Text(value="", color= "black", size=20) #Elementos compra
    page.add(t2)
    page.update()
    
    
ft.app(target=main, view=ft.WEB_BROWSER)
    