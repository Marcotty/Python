from collections import Counter
import functools

Elements = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def calculateStrength(hand):
    #print(hand)
    result = 0
    for elem in Counter(hand).most_common(5):
        result = result + elem[1]**2
        #print(result)
    #Five of a kind 5 cartes les memes -> val = 5*5=25
    # 4 cartes les memes -> val = 4*4 + 1 =17
    # 3 cartes les memes et 2 cartes différentes -> val = 3*3 + 1 +1 = 11
    # Two pair - 2 * 2 cartes les mêmes -> val = 2 * 2 +1 * 2 * 2 = 9
    # One pair - 1 * 2 cartes les mêmes -> val = 2 + 1 +1 +1 = 7
    #toutes les cartes distinctes -> val = 5
    return result

def compareStrength(a, b):
    if(calculateStrength(a[0]) > calculateStrength(b[0])):
        return 1
    elif(calculateStrength(a[0]) < calculateStrength(b[0])):
        return -1
    else:
        # force égale
        for i, j in zip(a[0], b[0]):
            if(Elements.index(i) < Elements.index(j)):
                # a > b
                return 1
            elif(Elements.index(i) > Elements.index(j)):
                return -1
        return 0
    
def resolveCamelCards(values):
    values.sort(key=functools.cmp_to_key(compareStrength))
    result = 0
    for i, elem in  enumerate(values, start = 1):
        result += int(elem[1]) * i
    
    return result


list = [('32T3K',765), ('T55J5',684), ('KK677',28), ('KTJJT',220), ('QQQJA',483)]

with open("Exercice/input_d7_2023.txt", "r") as f:
    list2 = f.readlines()

list3 = [element.strip().split(' ') for element in list2]
print(resolveCamelCards(list3))



