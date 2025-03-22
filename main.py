from pages.home import *
from change_route import change_route

def main(page: ft.Page):

    def change(route):

        page.views.clear()
        page.views.append(
            change_route(page)[page.route]
        )
        page.update()

    page.on_route_change = change
    page.go('/')


ft.app(target=main)