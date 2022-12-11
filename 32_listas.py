nomes = ['Caio','Ésley','Camila', 'João']

print(len(nomes))

nomes [0] = "Caio Sampaio"

print(nomes[0])

nomes.append('Maria')

print(nomes)


nomes = []

while True:
    nome = (input('Digite -1 para sair ou cadastre um nome: '))
    if nome == "-1":
        break
    
    nomes.append(nome)

print (nomes)