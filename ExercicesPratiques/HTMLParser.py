import re

def string_check(str):
    opening_tags = ["<br>","<i>","<div>","<a>"]
    closing_tags = ["</br>","</i>","</div>","</a>"]

    stack = []

    tags_list = re.split('(<[^>]*>)', str)[1::2] #récupérer les tags
    print("DEBUG1", re.split('(<[^>]*>)', str))
    print("DEBUG2", re.split('(<[^>]*>)'[1::2], str))
    for tag in tags_list:
        if tag in opening_tags:
            stack.append(tag)
        elif tag in closing_tags:
            pos = closing_tags.index(tag)
            if (len(stack) > 0) and (opening_tags[pos] == stack[len(stack)-1]): #si le tag ouvrant à la position du tag fermant est égal au tag ouvrant de la stack
                stack.pop() #on enleve le tag ouvrant correspondant => détecte tag ouvrant et tag fermant corrects
            else:
                continue #?
    if stack:
        return stack[-1].replace('<','').replace('>','') #retourner le dernier tag (problématique) en enlevant les <>
    return True


assert string_check("Test 1 <div> some text </div>") == True
print(string_check("Test 2 <div> some <a>text</a> </div>"))
