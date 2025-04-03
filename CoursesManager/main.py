import Ingredient, Recette, ListeCourses
import GUI.ListeCourses as ListeCoursesApp
import Stock

riz = Ingredient.Ingredient("Riz", 200, enStock = True)
poulet = Ingredient.Ingredient("Poulet", 150, enStock = True)
poivrons = Ingredient.Ingredient("Poivrons", 100, enStock = True)
carottes = Ingredient.Ingredient("Carottes", 100, enStock = True)

ingredientsBaseTest = [riz, poulet, poivrons, carottes]
for ing in ingredientsBaseTest:
    ing.quantite += 500
ingredientsAvailableTest = [riz, poulet, poivrons, carottes]
recetteTest = Recette.Recette("Riz au poulet et poivrons carottes", ingredientsBaseTest)
listeTest = ListeCourses.ListeCourse("Liste base", ingredientsBaseTest)
stock = Stock.Stock("stock_base.txt")
if(stock.ingredients != ingredientsAvailableTest):
    stock.ingredients = ingredientsAvailableTest
    stock.save()
print(recetteTest.isAvailable(ingredientsAvailableTest))

def choice():
    choix = input("Entree : ")
    if(choix == '1'):
      print(listeTest)
    if(choix == '2'):
        listeTest.ajouterIngredient()
    if(choix == '3'):
        listeTest.modifierIngredient()
    if(choix == '4'):
        listeTest.supprimerIngredient()
    if(choix == '5'):
        pass
    if(choix == '6'):
         stock.delete()
    return choix
      
def menu():
    print("Courses Manager :")
    print("1. Voir liste")
    print("2. Ajouter nouvel ingrédient")
    print("3. Modifier ingrédient")
    print("4. Supprimer ingrédient")
    print("6. Supprimer fichier stock")
    print("5. Quitter")
    choix = choice()
    return choix
 
        
if __name__ == '__main__':
    # ListeCourses.ListeCourse().run()
    
    choix = 0
    while(choix != '5'):
        choix = menu()
   