"""
Author:
    Gaming On Insulin

License:
    https://github.com/gamingoninsulin/WrapperCraft/blob/master/LICENSE.md

Made With:
    Python 3.9.7
    Visual Studio Code
    Kivy 2.0.0

Specials:
    Twitter: https://www.twitter.com/gamingoninsulin 
    GitHub: https://github.com/gamingoninsulin/WrapperCraft

Description: 
    A Minecraft Server manager called WrapperCraft made with Python.
"""
# IMPORTS
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file("kivy/wrappercraft.kv")

# Main Grid Layout
class MainLayout(GridLayout):
    
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    # Initialize infinite keywords
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)


    # passes the NAME PIZZA and COLOR inputs to "print to screen"
    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self .color.text
        
        # print to screen
        print(f"your name is {name} and you like {pizza} oh he nice {color} shoes.")


# Main class (build the app)
class WrapperCraft(App):
    def build(self):
        return MainLayout()


# calling the WrapperCraftMain to run the app
if __name__ == '__main__':
    WrapperCraft().run()
