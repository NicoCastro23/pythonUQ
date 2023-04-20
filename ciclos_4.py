y = lambda mensaje: int (input(mensaje))
x = y ("dar un numero:")
c = 0
while x > 0 :
    c += 1 
    x = x // 10
print(c) 