ingrese_real = lambda mensaje : int(input(mensaje))
def calcular_serie(n):
    resultado = 0
    signo = 1
    for i in range(1, n):
        elemento = i * 9 - (i // 2) * 4
        if n % 2 == 0:
            signo = 1
            resultado += signo * elemento
            print(elemento)
        else:
            signo *= -1
            resultado += signo * elemento
    return resultado

numero_uno = ingrese_real("Ingrese el límite inferior: ")
do = calcular_serie(numero_uno)
print(do)

