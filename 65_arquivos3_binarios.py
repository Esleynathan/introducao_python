import pickle
#TRANSFORMANDO EM BINARIO COM LISTA#
#x = [1, 2, 3, 4]
#string = pickle.dumps(x)
#print(string)
#RETORNANDO A ORIGINAL#
#print(pickle.loads(string))

#COM DICIONARIO#
#x = {'nome': 'ésley', 'idade': 20}
#string = pickle.dumps(x)
#print(type(pickle.loads(string)))

class  Pessoa:
    nome = 'Ésley'
    idade = 20

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoas('Ésley', 21)

x = [1, 2, 3, 4]
arq = open ('arquivo.pkl','ab')
pickle.dump(Pessoa, arq)

arq = open ('arquivo.pkl','rb')
retornou = pickle.load(arq)
print(retornou.idade)

retornou = pickle.load(arq)
print(retornou.idade)

