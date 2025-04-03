import Ingredient
import kivy
from kivy.app import App
from kivy.uix.label import Label
    
        
class ListeCourse(App):
    def __init__(self, Ingredients = None):
        self.Ingredients = Ingredients
        
    def build(self):
        return Label(text="Bienvenue dans Kivy !")
