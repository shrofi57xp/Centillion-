from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from brain import think
from speak import speak

class UI(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(orientation="vertical")

        self.input = TextInput()

        send = Button(text="Send")

        send.bind(on_press=self.ask)

        self.add_widget(self.input)

        self.add_widget(send)

    def ask(self, instance):

        answer = think(self.input.text)

        print(answer)

        speak(answer)