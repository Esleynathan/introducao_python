import os 

#x = lambda nome, idade: print (f'nome = {nome}\nidade = {idade}')
#x ('Ésley',20)

def teste():
    return lambda *idade: print(idade)

x = teste()

x('ésley')