x = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

#def fun(x):
#    return x < 18
# x = filter(func(x), x)

x = list(filter(lambda x: x < 18, x))
print(x)

y = [{'nome': 'Ésley', 'idade': 20}, {'nome': 'Ésley', 'idade': 40}]
y = list(filter(lambda y: y['idade'] >= 40, y))
print(y)