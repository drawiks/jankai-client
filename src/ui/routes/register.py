
import flet as ft

class RegisterRoute:
    def __init__(self):
        self.username_field = ft.TextField(label="Имя пользователя", width=250)
        self.password_field = ft.TextField(label="Пароль", width=250, password=True, can_reveal_password=True)
        self.email_field = ft.TextField(label="Электронная почта", width=250)
    
    def build(self, arg):
        self.username_field.value = None
        self.password_field.value = None
        self.email_field.value = None
        return ft.View(
            "/register",
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
                                self.email_field,
                                ft.TextButton(text="Уже есть аккаунт?", width=250, on_click=lambda e: e.page.go("/login")),
                                ft.ElevatedButton(text="Регистрация", width=250, on_click=lambda e: e.page.go("/"))
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
        )
