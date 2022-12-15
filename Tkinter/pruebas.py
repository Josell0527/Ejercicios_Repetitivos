import flet as ft

def main(page):
    def close_banner(e):
        page.banner.open = False
        page.update()

    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(color=ft.colors.AMBER, size=40),
        content=ft.Text(
            "Oops, there were some errors while trying to delete the file. What would you like me to do?"
        ),
        actions=[
            ft.TextButton("Finalizar", on_click=close_banner),
            ft.TextButton("Continuar comprando", on_click=close_banner),
        ],
    )

    def show_banner_click(e):
        page.banner.open = True
        page.update()

    page.add(ft.ElevatedButton("", on_click=show_banner_click))

ft.app(target=main)