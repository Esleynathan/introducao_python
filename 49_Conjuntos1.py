#x = [1,1,1,2,2,3,4,5]
#Covertendo uma lsita par aum set - Tudo que é repetido no conjunto é desconsiderado
#x = set(x)
#print (x)



x = {1, 2, 3, 4, 5}
y = {5, 6, 7, 8, 9, 10}

#t = x.union(y)
#t = x.intersection(y)
#t = x.difference(y)
t = x.symmetric_difference(y)

print(t)


