import flet as ft 


class Home(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.content = ft.Container(expand=True,content=ft.ElevatedButton(
            text='Login',
            bgcolor='red',
            on_click= lambda _: self.page.go('/login')
            
        ), alignment= ft.alignment.center)
