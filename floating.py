from kivy.uix.button import Button

class Floating(Button):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.text = "Centillion"

        self.size = (150,150)

    def on_press(self):

        print("Centillion Opened")