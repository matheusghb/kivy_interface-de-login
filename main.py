from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image, AsyncImage
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

class Login(Screen):
     
    def build (self):

        Window.clearcolor = (1,1,1,1)
        
        l = FloatLayout()

        ti = Label(text="Login", size_hint=(None, None), bold=True, pos_hint={'center_x':0.5, 'y':0.9}, font_name='Arial', color=(0,0,0,1))
        img = AsyncImage(source="https://cdn.icon-icons.com/icons2/37/PNG/512/contacts_3695.png", pos_hint={'center_x':0.5, 'y':0.6}, size_hint=(0.2,0.2))
        em = TextInput(hint_text='Email', pos_hint= {'center_x':0.5, 'y': 0.5}, size_hint=(0.4,0.05))
        reg = TextInput(hint_text="Senha", pos_hint= {'center_x':0.5, 'y':0.425}, size_hint=(0.4,0.05))
        env = Button(text='Enviar', size_hint=(0.1,0.05), pos_hint={'center_x':0.65, 'y':0.35}, background_color=get_color_from_hex('#2AA8CF'))
        btnr = Button(text="Registrar", size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'y':0.25})
        btnr.bind(on_press=root.manager.current='Registro')
        
        l.add_widget(ti)
        l.add_widget(img)
        l.add_widget(em)
        l.add_widget(reg)
        l.add_widget(env)
        l.add_widget(btnr)
        return l

class Registro(Screen):
    def build(self):
        Window.clearcolor = (1,1,1,1)

        l = FloatLayout()

class Sm(App):
    def build(self):
     sm = ScreenManager()

     sm.add_widget(Login(name='Login'))
     sm.add_widget(Registro(name='Registro'))
    
if __name__ == "__main__":
    Sm().run()
