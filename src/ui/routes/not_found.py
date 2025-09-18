import flet as ft

class NotFoundRoute:
    def build(self, navigation_rail):
        return ft.View(
            "/404",
            [
                ft.Container(
                    content=
                        ft.Row(
                            [
                                navigation_rail,
                                ft.Column(
                                    [
                                        ft.Text("Страница не найдена", size=30, color=ft.Colors.GREEN_ACCENT_200),
                                    ]
                                )
                            ],
                        ),
                        expand=True
                ),
                
            ]
        )
