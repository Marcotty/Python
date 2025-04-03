import os

class Stock():
    def __init__(self, stock_file):
        self.stock_file = stock_file
        try:
            print("Ouverture fichier Stock ", stock_file)
            f = open(stock_file, "r")
            self.ingredients = f.readlines()
            print(self.ingredients)
            f.close()
        except:
            print("Pas de fichier de stock détecté. Création nouveau fichier.")
            f = open(stock_file, "x")
            f.close()
            self.ingredients = []
    
    def save(self):
        print("Sauvegarde de la liste : ")
        [print(str(ingredient) + "\n") for ingredient in self.ingredients]
        with open(self.stock_file, "w") as f:
            f.writelines([str(ingredient) + "\n" for ingredient in self.ingredients])

    def delete(self):
        os.remove(self.stock_file)