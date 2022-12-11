x = [1,2,3]
y = x
z = x.copy()
y[0] = 0


print (x),print(hex(id(x)))
print (y),print(hex(id(y)))
print (z),print(hex(id(z)))