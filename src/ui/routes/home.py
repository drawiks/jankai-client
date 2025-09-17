import flet as ft

class HomeRoute:
    def __init__(self):
        self.post_column = ft.Column(spacing=20)
        self.post_field = ft.TextField(label="Что у вас нового?", multiline=True, max_lines=10, width=750, border_radius=15)
    
    def build(self, navigation_rail):
        return ft.View(
            "/",
            [
                ft.Container(
                    content=ft.Row(
                        [
                            navigation_rail,
                            ft.Column(
                                [
                                    self.post_field,
                                    ft.Row([
                                            ft.ElevatedButton("Опубликовать"),
                                            ft.IconButton(icon=ft.Icons.ADD_PHOTO_ALTERNATE_OUTLINED),
                                            ft.IconButton(icon=ft.Icons.ATTACH_FILE)
                                    ]),
                                    ft.Divider(thickness=1),
                                    self.post_column,
                                ]
                            )
                        ],
                    ),
                    expand=True
                ),
                
            ]
        )
