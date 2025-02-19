from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

class MainView(MDScreen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.build_ui()

    def build_ui(self):
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)
        message = self.controller.get_message()
        label = MDLabel(
            text=message,
            halign="center",
            theme_text_color="Primary",
            font_style="H4"
        )
        layout.add_widget(label)
        self.add_widget(layout)