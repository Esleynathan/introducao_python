pessoa = {'nome': 'Ésley Nathan','idade': 21, 'altura': 173}

print (pessoa.values())
print (pessoa.keys())
print (pessoa.items())

#for i in pessoa.tems():
#    print (i[0],i[1])

for i, j in pessoa.items():
    print(f'i = {i} j = {j}')

