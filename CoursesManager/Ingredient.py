# nom
# quantité
# image
# enStock
class Ingredient:
    def __init__(self, name, quantite = 0, image = None, enStock = False):
        self.name = name
        self.quantite = quantite
        self.image = image
        self.enStock = enStock
        
    def __str__(self):
        return f"{self.name}({self.quantite}g) enStock: {self.enStock}"   
    
    def modifierIngredient(self):
        name = input("Nom : ")
        quantite = input("Quantité : ")
        enStock = input("En stock : ")
        if enStock == '1' or enStock == "Oui" or enStock == "oui":
            enStock = True
        else:
            enStock = False
        image = input("Image : ")
        image = None
        return Ingredient(name, quantite, image, enStock)
    
def newIngredientMenu():
    print("Nouvel ingredient:")
    name = input("Nom : ")
    quantite = input("Quantité : ")
    enStock = input("En stock : ")
    if enStock == '1' or enStock == "Oui" or enStock == "oui":
        enStock = True
    else:
        enStock = False
    image = input("Image : ")
    image = None
    return Ingredient(name, quantite, image, enStock)