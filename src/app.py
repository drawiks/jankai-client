
import flet as ft

from routes import HomeRoute

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.title = "jankai"
        
        self.page.on_route_change = lambda e: self.route_change(self.page.route)
        self.page.on_view_pop = self.view_pop
        
        self.page.go("/")
        
        self.routes = {
            "/": HomeRoute()
        }
        
        self.navigation_rail = ft.NavigationRail(
            destinations=[
                ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationRailDestination(icon=ft.Icons.ACCOUNT_CIRCLE, label="Profile"),
                ft.NavigationRailDestination(icon=ft.Icons.PEOPLE_ALT, label="Friends"),
                ft.NavigationRailDestination(icon=ft.Icons.SEARCH, label="Search"),
                ft.NavigationRailDestination(icon=ft.Icons.NOTIFICATIONS, label="Notifications"),
                ft.NavigationRailDestination(icon=ft.Icons.MESSENGER, label="Messenger"),
            ],
            selected_index=0,
            on_change=self.on_rail_change,
        )

    def on_rail_change(self, e):
        self.page.go("/")
        
    def route_change(self, route):
        self.page.views.clear()
        if route in self.routes:
            self.page.views.append(self.routes[route].build(self.navigation_rail))
        else:
            self.page.views.append(self.not_found_route.build())
        self.page.update()
        
    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

if __name__ == "__main__":
    ft.app(App, view=ft.WEB_BROWSER)