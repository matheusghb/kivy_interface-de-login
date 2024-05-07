from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex

class MinhaApp(App):
    
    def build (self):
        Window.clearcolor = (1,1,1,1)
        
        l = FloatLayout()
        img = Image(source="/Users/aluno.sesipaulista/Downloads/contatoicone.png", pos_hint={'center_x':0.5, 'y':0.7}, size_hint=(0.2,0.2))
        log = TextInput(hint_text='Email', pos_hint= {'center_x':0.5, 'y': 0.6}, size_hint=(0.6,0.05))
        reg = TextInput(hint_text="Senha", size_hint=(0.6,0.05)
        env = Button(text='Enviar', size_hint=(0.1,0.1), halign='center', background_color=get_color_from_hex('#2AA8CF'))
        btnl = Button(text="Login", size_hint=(0.2,0.3), halign='center')
        btnr = Button(text="Registrar", size_hint=(0.2,0.3), halign='center')
        
        l.add_widget(img)
        l.add_widget(log)
        l.add_widget(reg)
        l.add_widget(env)
        l.add_widget(btnl)
        l.add_widget(btnr)
        return l

if __name__ == "__main__":
    MinhaApp().run()