pessoas = []

while True:
    decisao = int('Digite 1 para cadastrar uma pessoa e 2 par sair:')
    if decisao == 2:
        break
    pessoa = {'nome:': input('Digite o nome:'),
             'idade:': input('Digite a idade'),
             'altura:': input('Digite a altura:')}

    pessoas.append(pessoa)

print(pessoas)
