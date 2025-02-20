from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

class MainView(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Use the function to create the top app bar
        top_app_bar = app.create_top_app_bar("Home Page")
        layout.add_widget(top_app_bar)

        # >>>>>>>>>> Page Content >>>>>>>>>>
        layout.add_widget(MDLabel(text="This is the Home Page", halign="center", font_style='H5'))
        # <<<<<<<<<< Page Content <<<<<<<<<<
        
        self.add_widget(layout)