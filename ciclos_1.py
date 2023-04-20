"""""
x = lambda mensaje : int (input(mensaje))
give_numbre = x("ingrese un numero n:")
for i in range (6,give_numbre,3):
    print (i)
"""""
""""
x = lambda mensaje : str (input(mensaje))

give_number = x ("digite el numero:")

x = len (give_number)
print (x)

"""

""""
x = lambda mensaje : int(input(mensaje))
give_number = x("numero 1:") # 3
give_number_two = x("numero 2:") # 4
z = 0 
for i in range(0, give_number_two):
    z += give_number # 3+3+3+3
    print(z)
"""
y = lambda mensaje: int (input(mensaje))
x = y ("dar un numero:")
c = 0
while x > 0 :
    c += 1 
    x = x // 10
print(c) 