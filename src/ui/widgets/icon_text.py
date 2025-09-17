
import flet as ft
from flet.core.types import OptionalNumber, OptionalString

class IconText(ft.Row):
    def __init__(
        self,
        # ---icon---
        icon: ft.Icons = None, 
        icon_color: ft.Colors = None,
        icon_size: OptionalNumber = None,
        
        # ---text---
        text: OptionalString = None,
        text_align: ft.TextAlign = None,
        font_family: OptionalString = "plex medium",
        
        # ---row---
        aligment: ft.MainAxisAlignment = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        visible: bool = True,
        
        # ---icontext---
        position: bool = True
    ):
        super().__init__(
            alignment=aligment,
            visible=visible,
            width=width,
            height=height
        )
        
        self.icon = ft.Icon(
            name=icon,
            color=icon_color,
            size=icon_size,
        )
        self.text = ft.Text(
            value=text,
            text_align=text_align,
            font_family=font_family
        )
        
        if position:
            self.controls = [
                self.icon,
                self.text
            ]
        else:
            self.controls = [
                self.text,
                self.icon
            ]