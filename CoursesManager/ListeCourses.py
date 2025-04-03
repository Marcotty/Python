import Ingredient
    
        
class ListeCourse():
    def __init__(self, name, Ingredients = None):
        self.name = name
        self.Ingredients = Ingredients
        
    def __str__(self):
        return f"Liste : {self.name}\n" + "".join([str(ingredient[0] + 1) + ". " + str(ingredient[1]) + "\n" for ingredient in enumerate(self.Ingredients)])

    def ajouterIngredient(self):
        self.Ingredients.append(Ingredient.newIngredientMenu())
    def modifierIngredient(self):
        choix = input("Entrer ingredient : ")
        self.Ingredients[int(choix)-1] = self.Ingredients[int(choix)-1].modifierIngredient()
    def supprimerIngredient(self):
        choix = input("Entrer ingredient : ")
        self.Ingredients.remove(self.Ingredients[int(choix)-1])