arquivo = open('pessoas.txt', 'a')
i = 0
while True:
    if i > 1:
        break
    arquivo.write(input('Digite o nome da pessoa: ') + input('Digite a idade: ') + "\n")

    i += 1

#arquivo = open(pessoas.txt, 'r')
#resultados = arquivos.read()
#print(resultados)

#x = []
#for i2 in resultados:
#    x.append(i2.split())
#print(x)    