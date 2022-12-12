#def soma_numeros(n1,n2):
#    print (n1 + n2)
#soma_numeros(5,2)
#soma_numeros(n2 = 10, n1 = 5)


#def soma_numeros(n1, n2, *args):
#    print(f'n1 = {n1} n2 = {n2} args  = {args}')


#def soma_numeros(*args):
#    soma = 0
#    for i in args:
#        soma = soma + i
#    print (soma)

def soma_numeros(**kwargs):
    x = kwargs.get('teste4')
    if x:
        print('Foi passado.')
    else:
        print('Não foi passado.')

soma_numeros(teste1 = 1, teste2 = 2, teste3 = 3, teste4  = 4)
