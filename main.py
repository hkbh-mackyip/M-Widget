from kivymd.app import MDApp
from kivy.core.window import Window
from controllers.main_controller import MainController
from views.main_view import MainView

class MWidget(MDApp):
    def build(self):
        # Window.maximize()
        controller = MainController()
        return MainView(controller=controller)

if __name__ == '__main__':
    MWidget().run()