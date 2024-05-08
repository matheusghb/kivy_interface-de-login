from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image, AsyncImage
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

class Registro(App):
         def build(self):

                Window.clearcolor = (1,1,1,1)

                l = FloatLayout()

                r = Label(text="Registro", size_hint=(None, None), pos_hint={'x':0.5, 'y':0.85}, color=(0,0,0,1), bold=True, size=(100,100))
                img = Image(source="", pos_hint={'x':0.5, 'y':0.8})

                ln = Label(text='Nome:', size_hint=(None, None), pos_hint={'x':0.2, 'y':0.680}, color=(0,0,0,1), bold=True, size=(70,70))
                tn = TextInput(pos_hint={'center_x':0.6, 'y':0.7 }, size_hint=(0.55,0.05))
                le = Label(text="E-mail:", size_hint=(None,None), pos_hint={'x':0.2,'y':0.580}, color=(0,0,0,1), bold=True, size=(70,70))
                te = TextInput(pos_hint={'center_x':0.6, 'y':0.6}, size_hint=(0.55, 0.05))
                lc = Label(text="Celular:", size_hint=(None,None), pos_hint={'x':0.2, 'y':0.480}, color=(0,0,0,1), bold=True, size=(70,70))
                tc = TextInput(pos_hint={'center_x':0.6, 'y':0.5}, size_hint=(0.55, 0.05))
                ls = Label(text='Senha:', size_hint=(None, None), pos_hint={'x':0.2, 'y':0.380}, color=(0,0,0,1), bold=True, size=(70,70))
                ts = TextInput(pos_hint={'center_x':0.6, 'y':0.4}, size_hint=(0.55, 0.05))
                l.add_widget(r)
                l.add_widget(ln)
                l.add_widget(tn)
                l.add_widget(le)
                l.add_widget(te)
                l.add_widget(lc)
                l.add_widget(tc)
                l.add_widget(ls)
                l.add_widget(ts)

                return l
    
if __name__ == "__main__":
    Registro().run()