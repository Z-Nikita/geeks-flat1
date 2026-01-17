import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    text_hello = ft.Text(value='Hello World')
    name_input = ft.TextField(label="Введите имя", on_submit=lambda e: text_name(e))

    def text_name(_):
        # print(name_input.label)
        name = name_input.value.strip()


        if name:
            timestamp = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
            text_hello.color = None
            text_hello.value = f"{timestamp} - Hello, {name}!"
            name_input.value = ""
        else:
            text_hello.value = "Введите имя!"
            text_hello.color = ft.Colors.RED

    elevated_button = ft.ElevatedButton('send', on_click=text_name, icon=ft.Icons.SEND, color=ft.Colors.RED, icon_color=ft.Colors.BLACK)

    name_input = ft.TextField(label='Введите что-нибудь', on_submit=text_name)

    def thememode(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK

    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

    # добавление на страницу
    page.add(text_hello, name_input, elevated_button, thememode_button)


ft.app(target=main)