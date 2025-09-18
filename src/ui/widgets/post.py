
import flet as ft
from flet.core.types import OptionalNumber, OptionalString, OptionalControlEventCallable

class Post(ft.Container):
    def __init__(
        self,
        post_author: OptionalString = None,
        post_text: OptionalString = None,
        # ---align---
        aligment: ft.alignment = None,
        # ---styling---
        bgcolor: ft.Colors = None,
        border_radius: OptionalNumber = 15,
        # ---spacing---
        margin: OptionalNumber = None,
        padding: OptionalNumber = None,
        # ---geometry---
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        # ---event---
        on_click: OptionalControlEventCallable = None,
    ):
        super().__init__(
            alignment=aligment,
            bgcolor=bgcolor,
            border_radius=border_radius,
            margin=margin,
            padding=padding,
            width=width,
            height=height,
            on_click=on_click
        )
        
        self.text = ft.Text(
            value=post_text,
            no_wrap=False,
            size=20,
        )
        self.author = ft.TextButton(
            text=post_author,
            size=20,
        )
        
        self.content = ft.Column(
            controls=[
                ft.Row(
                    [
                        self.author,
                        ft.Text("Sep 18")
                    ]
                ),
                self.text
            ]
        )
        