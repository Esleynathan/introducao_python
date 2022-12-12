x = [i for i in range(12, 26)]    
x = list(map(lambda x: 666 if x < 18 else(x), x))
print(x)

y = [{'nome': 'Ésley', 'idade': 20}, {'nome': 'Ésley', 'idade': 22}]
y = list(map(lambda y: {'nome': y['nome'], 'idade':'menor do que 30 anos'} if y['idade'] < 30 else (y), y))
print (y)