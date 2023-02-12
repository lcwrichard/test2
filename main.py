from kivymd.app import MDApp 
from kivy.uix.button import Button 

class Main_App(MDApp):
    def build(self):
        return Button(text='Hello World')

Main_App().run()        