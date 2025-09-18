
import flet as ft

class HomeRoute:
    def __init__(self):
        self.post_column = ft.Column(spacing=20)
        self.post_field = ft.TextField(label="Что у вас нового?", multiline=True, max_lines=10, width=750, border_radius=15)
    
    
    def create_post(self, e):
        if len(self.post_field.value) <= 5:
            return
        else:
            self.post_column.controls.append(
                ft.Text(self.post_field.value)
            )
            self.post_field.value = None
        e.page.update()

    def build(self, navigation_rail):
        return ft.View(
            "/",
            [
                ft.Container(
                    content=ft.Row(
                        [
                            navigation_rail,
                            ft.Container(
                                content=ft.Column(
                                    [ 
                                        ft.Container(height=20),
                                        self.post_field,
                                        ft.Row([
                                                ft.ElevatedButton("Опубликовать", on_click=self.create_post),
                                                ft.IconButton(icon=ft.Icons.ADD_PHOTO_ALTERNATE_OUTLINED),
                                                ft.IconButton(icon=ft.Icons.ATTACH_FILE)
                                        ]),
                                        ft.Divider(thickness=1),
                                        self.post_column,
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    scroll=ft.ScrollMode.ADAPTIVE
                                ),
                            ),
                            
                        ],
                        spacing=25
                    ),
                    expand=True
                ),
                
            ]
        )
