from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class MinhaApp(App):
    def build (self):
        Window.clearcolor = (1,1,1,1)
        
        l = BoxLayout(orientation="vertical", padding=20, spacing=[20,10])
        img = Image(source='/Users/aluno.sesipaulista/Downloads/contatoicone.jpg')
        btnl = Button(text="Login")
        btnr = Button(text="Registrar")
        l.add_widget(img)
        l.add_widget(btnl)
        l.add_widget(btnr)


if __name__ == "__main__":
    MinhaApp().run()