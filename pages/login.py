import flet as ft 


class Login(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.app_bar = ft.Container(
            alignment=ft.alignment.bottom_center,
            height=80,
            bgcolor=ft.Colors.BLACK,
            content= ft.Row(
                alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Container(padding=20,content=ft.Text('Sistema Login', style=ft.TextStyle(color=ft.Colors.BLUE, size=15, weight=ft.FontWeight.BOLD))),
                    ft.Row(controls=[ft.TextButton(text='Login'), ft.TextButton(text='Cadastrar')])
                    ]
            )
        )
        column = ft.Container(margin=ft.margin.only(top=100),height=350, width=350, shadow=ft.BoxShadow(
                blur_radius=20,
                color=ft.Colors.BLACK
            ) ,content=ft.Column(
            controls=[
                ft.Text('LOGIN', style=ft.TextStyle(size=30, weight=ft.FontWeight.BOLD)),
                ft.Container(ft.TextField(
                    hint_text='Email'
                ), width=300),
                ft.Container(ft.TextField(
                    hint_text='Senha'
                ), width=300),
                ft.Container(margin=ft.margin.only(top=20), content=ft.ElevatedButton(
                    text='Login',
                    width=150,
                    bgcolor='green'
                
                ))
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        ),border=ft.border.all(5), bgcolor="#247cc3", border_radius=ft.border_radius.all(15))

        

        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                self.app_bar, column
            ]
        )