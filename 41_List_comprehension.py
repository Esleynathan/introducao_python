#x = [[input() for j in range(4,7)] for i in range(0,3)]

#x = [input('Digite um nome:') for i in range (0, 10)]


x = [i for i in range(0,10) if i > 4]

print(x)


y = []
for i in range(0,10):
    if i > 4:
        y.append(i)