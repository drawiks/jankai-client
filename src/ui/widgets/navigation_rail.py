
import flet as ft

class NavigationRail(ft.NavigationRail):
    def __init__(self, destinations = None, elevation = None, selected_index = None, extended = None, label_type = None, bgcolor = None, indicator_color = None, indicator_shape = None, leading = None, trailing = None, min_width = None, min_extended_width = None, group_alignment = None, selected_label_text_style = None, unselected_label_text_style = None, on_change = None, ref = None, width = None, height = None, left = None, top = None, right = None, bottom = None, expand = None, expand_loose = None, col = None, opacity = None, rotate = None, scale = None, offset = None, aspect_ratio = None, animate_opacity = None, animate_size = None, animate_position = None, animate_rotation = None, animate_scale = None, animate_offset = None, on_animation_end = None, visible = None, disabled = None, data = None, rtl = False):
        super().__init__(destinations, elevation, selected_index, extended, label_type, bgcolor, indicator_color, indicator_shape, leading, trailing, min_width, min_extended_width, group_alignment, selected_label_text_style, unselected_label_text_style, on_change, ref, width, height, left, top, right, bottom, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, visible, disabled, data, rtl)
        self.on_change = on_change
        self.selected_index = 0
        self.destinations = [
            ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationRailDestination(icon=ft.Icons.ACCOUNT_CIRCLE, label="Profile"),
            ft.NavigationRailDestination(icon=ft.Icons.SEARCH, label="Search"),
        ]