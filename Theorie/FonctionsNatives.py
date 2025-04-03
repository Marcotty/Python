
'''
    Enumerate
    Permet de renvoie un iterable associant l'index et l'objet de la liste
    
    def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1
'''
list = ['a', 'b', 'c', 'd']

for i in enumerate(list):
    print(i)
    
    
    
'''
    Zip
'''