
import flet as ft

class LoginRoute:
    def __init__(self):
        self.username_field = ft.TextField(label="Имя пользователя", width=250)
        self.password_field = ft.TextField(label="Пароль", width=250, password=True, can_reveal_password=True)
    
    def build(self, arg):
        self.username_field.value = None
        self.password_field.value = None
        return ft.View(
            "/login",
            [
                ft.Row(
                    [
                        ft.Column(
                            controls=[
                                ft.Text(
                                    "jankai",
                                    size=50,
                                    color=ft.Colors.LIGHT_GREEN_300,
                                    weight=ft.FontWeight.W_100,
                                    text_align=ft.TextAlign.CENTER,
                                    font_family="jersey"
                                ),
                                self.username_field,
                                self.password_field,
                                ft.TextButton(text="Нет аккаунта?", width=250, on_click=lambda e: e.page.go("/register")),
                                ft.ElevatedButton(text="Вход", width=250, on_click=lambda e: e.page.go("/"))
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
        )
