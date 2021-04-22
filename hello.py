# * 
# ！

import kivy
kivy.require('2.0.0') # 用你当前的kivy版本替换

from kivy.app import App
from kivy.uix.label import Label

class HelloApp(App):
    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__':
    HelloApp().run()