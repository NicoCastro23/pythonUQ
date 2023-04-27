import functools
give_integer = lambda mensaje : int (input(mensaje))#lamda para fragmentar el codigo el cual nos permite ingresar un integer
lista = [0, 9, -4, 15, -8, 21, -12, 27, -16, 33, -20]
numero_uno = give_integer("Ingrese el límite inferior: ")
result = functools.reduce(lambda counter, item : counter + item, lista[0 : numero_uno])
print(result)