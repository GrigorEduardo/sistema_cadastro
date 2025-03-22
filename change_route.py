from pages.home import Home
from pages.login import Login
import flet as ft

def change_route(page:ft.Page):
    return {
        '/' : ft.View(
            route='/',
            controls=[Home(page)],
            padding=0,
        ),
        '/login' : ft.View(
            route='/login',
            controls=[Login(page)],
            padding=0,
        )
    }