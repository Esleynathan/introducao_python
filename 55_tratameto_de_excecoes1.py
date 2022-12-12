n1 = int(input('Digite um numero:'))
n2 = int(input('Digite um numero:'))

try:
    print(n1/n2)
except:
    print('Não consegui.')
finally:
    print('Finalizado!')