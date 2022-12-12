try:
    x = int(input('Digite um numero:'))
    print (5/x)
except ValueError:
    print('Digite um numoero inteiro!')
except ZeroDivisionError:
    print('Não digite 0!')
finally:
    print('Finalizado!')