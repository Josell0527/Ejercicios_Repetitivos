import flet as ft


def main(page):

    page.snack_bar = ft.SnackBar(
        content=ft.Text("Hello, world!"),
        action="Alright!",
    )

    def on_click(e):
        page.snack_bar = ft.SnackBar(ft.Text(f"Hello"))
        page.snack_bar.open = True
        page.update()

    page.add(ft.ElevatedButton("Open SnackBar", on_click=on_click))

ft.app(target=main)
