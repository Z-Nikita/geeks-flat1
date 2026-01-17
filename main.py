import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    text_hello = ft.Text(value='Hello World')
    name_input = ft.TextField(label="Введите имя", on_submit=lambda e: text_name(e))

    greeting_history = []
    history_text = ft.Text('История приветствий:')

    def text_name(_):
        # print(name_input.label)
        name = name_input.value.strip()


        if name:
            timestamp = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
            text_hello.color = None
            text_hello.value = f"{timestamp} - Hello, {name}!"
            name_input.value = ""
            greeting_history.append(name)
            print(greeting_history)
            history_text.value = 'История приветствий:\n' + '\n'.join(greeting_history)
        else:
            text_hello.value = "Введите имя!"
            text_hello.color = ft.Colors.RED

    elevated_button = ft.ElevatedButton('send', on_click=text_name, icon=ft.Icons.SEND, color=ft.Colors.RED, icon_color=ft.Colors.BLACK)

    name_input = ft.TextField(label='Введите что-нибудь', on_submit=text_name, expand=True)

    def thememode(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK

    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)

    def clear_history(_):
        print(greeting_history)
        greeting_history.clear()
        print(greeting_history)
        history_text.value = 'История приветствий:'

    def delete_last(_):
        if greeting_history:
            greeting_history.pop()
            history_text.value = 'История приветствий:\n' + '\n'.join(greeting_history) if greeting_history else 'История приветствий:'
            text_hello.value = "Удалено последнее приветствие."
            text_hello.color = None
        else:
            text_hello.value = "История пуста!"
            text_hello.color = ft.Colors.RED

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    delete_last_button = ft.ElevatedButton("Удалить последнее", on_click=delete_last)
    main_object = ft.Row([name_input, elevated_button, thememode_button, delete_last_button, clear_button])

    # добавление на страницу
    page.add(text_hello, main_object, history_text)


ft.app(target=main)