import flet as ft

def main(page: ft.Page):
    page.add(ft.Image(src=f"/imagenes/imagen.png"))


ft.app(target=main, assets_dir="imagenes")