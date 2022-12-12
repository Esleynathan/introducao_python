from pympler.asizeof import asizesof

#def dobro(lista):
#    lista_dobro = []
#    for i in lista:
#       lista_dobro.append(i*2) 
#    
#    return lista_dobro


#def dobro():
#    i = 0
#    while True:
#        i = i + 1
#        yield i
#x = dobro()

def dobro(lista):
    for i in lista:
        yield i*2

x = dobro (range(0,100))
print(asizesof(x))


def dobro2(lista):
    lista_2 = []
    for i in lista:
        lista_2.append(i)
    return lista_2

y = dobro2 (range(0,100))
print(asizesof(y))


#Iterando sobre os valores e tratnado o erro.
while True:
    try:
        print(next(x))
    except StopIteration:
        break


