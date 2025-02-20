from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar

class MainView(MDScreen):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller
        self.build_ui()

    def build_ui(self):
        layout = MDBoxLayout(orientation='vertical', padding=0, spacing=0)

        # Create the toolbar
        toolbar = MDTopAppBar(title="M Widget")
        toolbar.pos_hint = {"top": 1}
        layout.add_widget(toolbar)

        # Create the label
        message = self.controller.get_message()
        label = MDLabel(
            text=message,
            halign="center",
            theme_text_color="Primary",
            font_style="H4"
        )
        layout.add_widget(label)

        self.add_widget(layout)