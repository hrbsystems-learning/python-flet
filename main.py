import flet as ft
import time

class MedicineDispenserApp:
    def __init__(self):
        self.page = None
        self.language = "en"  # Default language
        self.translations = {
            "en": {
                "app_title": "Lar Alvorecer Medicine Dispenser",
                "login": "Login",
                "email": "Email",
                "password": "Password",
                "login_button": "Log In",
                "language": "Language",
                "stock_count": "Items in stock: {}",
                "details": "Details",
                "delete": "Delete",
                "dispense": "Dispense",
            },
            "pt": {
                "app_title": "Dispensador de Medicamentos Lar Alvorecer",
                "login": "Entrar",
                "email": "E-mail",
                "password": "Senha",
                "login_button": "Entrar",
                "language": "Idioma",
                "stock_count": "Itens em estoque: {}",
                "details": "Detalhes",
                "delete": "Excluir",
                "dispense": "Dispensar",
            }
        }

    def main(self, page: ft.Page):
        self.page = page
        self.page.title = self.translations[self.language]["app_title"]
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.window_width = 400
        self.page.window_height = 800
        self.page.window_resizable = False

        self.show_splash_screen()

    def show_splash_screen(self):
        splash = ft.Container(
            content=ft.Image(src="/path/to/your/splash_image.png"),
            width=400,
            height=800,
            alignment=ft.alignment.center
        )
        self.page.add(splash)
        self.page.update()
        time.sleep(2)  # Show splash for 2 seconds
        self.page.controls.clear()
        self.show_language_selection()

    def show_language_selection(self):
        def change_language(e):
            self.language = language_dropdown.value
            self.page.title = self.translations[self.language]["app_title"]
            self.show_login_page()

        language_dropdown = ft.Dropdown(
            label=self.translations[self.language]["language"],
            width=200,
            options=[
                ft.dropdown.Option("en", "English"),
                ft.dropdown.Option("pt", "Português"),
            ],
            value=self.language,
            on_change=change_language
        )

        self.page.add(ft.Container(content=language_dropdown, alignment=ft.alignment.center))
        self.page.update()

    def show_login_page(self):
        self.page.controls.clear()

        def login(e):
            # Here you would implement actual login logic
            self.show_main_page()

        email_field = ft.TextField(label=self.translations[self.language]["email"])
        password_field = ft.TextField(label=self.translations[self.language]["password"], password=True)
        login_button = ft.ElevatedButton(text=self.translations[self.language]["login_button"], on_click=login)

        self.page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text(self.translations[self.language]["login"], size=24),
                    email_field,
                    password_field,
                    login_button
                ]),
                alignment=ft.alignment.center
            )
        )
        self.page.update()

    def show_main_page(self):
        self.page.controls.clear()

        # Header
        header = ft.Container(
            content=ft.Column([
                ft.Text(self.translations[self.language]["app_title"], size=20, weight=ft.FontWeight.BOLD),
                ft.CircleAvatar(foreground_image_url="/path/to/your/logo.png"),
                ft.Text(self.translations[self.language]["stock_count"].format(100))  # Replace with actual count
            ]),
            padding=10,
            bgcolor=ft.colors.BLUE_100
        )

        # Medicine cards
        medicine_list = ft.ListView(spacing=10, padding=20, auto_scroll=True)
        for i in range(20):  # Example: 20 medicine cards
            medicine_list.controls.append(self.create_medicine_card(f"Medicine {i+1}"))

        self.page.add(
            header,
            medicine_list
        )
        self.page.update()

    def create_medicine_card(self, name):
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Image(src="/path/to/medicine/image.png", width=100, height=100),
                    ft.Text(name, size=16, weight=ft.FontWeight.BOLD),
                    ft.Text("Description line 1"),
                    ft.Text("Description line 2"),
                    ft.Text("Description line 3"),
                    ft.Text("Description line 4"),
                    ft.Row([
                        ft.ElevatedButton(text=self.translations[self.language]["details"], bgcolor=ft.colors.GREEN),
                        ft.ElevatedButton(text=self.translations[self.language]["delete"], bgcolor=ft.colors.RED),
                        ft.ElevatedButton(text=self.translations[self.language]["dispense"], bgcolor=ft.colors.BLUE),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                ]),
                padding=10
            )
        )

if __name__ == "__main__":
    app = MedicineDispenserApp()
    ft.app(target=app.main)
