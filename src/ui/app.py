
import flet as ft

from .widgets import (
    NavigationRail,
)

from .routes import (
    HomeRoute,
    ProfileRoute,
    LoginRoute,
    RegisterRoute,
    NotFoundRoute
)

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "jankai"
        self.page.fonts = {
            "jersey": "/fonts/Jersey20-Regular.ttf",
            "plex bold": "/fonts/IBMPlexSans-Bold.ttf",
            "plex medium": "/fonts/IBMPlexSans-Medium.ttf"
        }
        
        self.routes = {
            "/": HomeRoute(),
            "/profile": ProfileRoute(),
            "/login": LoginRoute(),
            "/register": RegisterRoute(),
        }
        self.not_found_route = NotFoundRoute()
        
        self.page.on_route_change = lambda e: self.route_change(self.page.route)
        self.page.on_view_pop = self.view_pop
        self.page.go("/")
        
        self.navigation_rail = NavigationRail(on_change=self.on_rail_change)

    async def on_rail_change(self, e):
        routes = ["/", "/profile", "/search"]
        self.page.go(routes[e.control.selected_index])
    
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
