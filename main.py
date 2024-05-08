from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image, AsyncImage
from kivy.utils import get_color_from_hex

class MinhaApp(App):
    
    def build (self):
        Window.clearcolor = (1,1,1,1)
        
        l = FloatLayout()
        img = AsyncImage(source="https://cdn.icon-icons.com/icons2/37/PNG/512/contacts_3695.png", pos_hint={'center_x':0.5, 'y':0.7}, size_hint=(0.2,0.2))
        log = TextInput(hint_text='Email', pos_hint= {'center_x':0.5, 'y': 0.6}, size_hint=(0.4,0.05))
        reg = TextInput(hint_text="Senha", pos_hint= {'center_x':0.5, 'y':0.525}, size_hint=(0.4,0.05))
        env = Button(text='Enviar', size_hint=(0.1,0.05), pos_hint={'center_x':0.65, 'y':0.45}, background_color=get_color_from_hex('#2AA8CF'))
        btnl = Button(text="Login", size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'y':0.25})
        btnr = Button(text="Registrar", size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'y':0.2})
        
        l.add_widget(img)
        l.add_widget(log)
        l.add_widget(reg)
        l.add_widget(env)
        l.add_widget(btnl)
        l.add_widget(btnr)
        return l

if __name__ == "__main__":
    MinhaApp().run()