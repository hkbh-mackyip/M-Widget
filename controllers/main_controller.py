from models.hello_model import HelloModel

class MainController:
    def __init__(self):
        self.model = HelloModel()

    def get_message(self):
        return self.model.get_message()