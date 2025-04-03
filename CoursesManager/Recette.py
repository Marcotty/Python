import Ingredient

class Recette:
    def __init__(self, name, ingredientsBase):
        self.name = name
        self.ingredientsBase = ingredientsBase
        
    def isAvailable(self, stock) -> bool:
        flag = 1
        
        return bool(flag)