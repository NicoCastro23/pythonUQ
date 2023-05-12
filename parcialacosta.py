from apoyo import ingresar_entero_mayor_que, mostrar_mensaje, ingresar_entero
"FALTO LO DE APOYO PERO USTEDES SABEN COMO ES"
#Ejercicio 1 a)
def sumar_impares(n):
    suma = 0
    for i in range(n):
        if i % 2 != 0:
            suma += i
    return suma
#Ejercicio 1 b)
def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado
#Ejercicio 2
def main():
    valor= ingresar_entero("Ingrese un número entero positivo: ")
    n = ingresar_entero_positivo(valor)
    mensaje = generar_mensaje(n)
    mostrar_mensaje(mensaje)

def ingresar_entero(cantidad):
    valor= int(input(cantidad))
    return valor

def ingresar_entero_positivo(cantidad):
    while True:
        try:
            valor = cantidad
            if valor <= 0:
                print("El número debe ser positivo.")
            else:
                return valor
        except ValueError:
            print("Debe ingresar un número entero válido.")

def generar_mensaje(n):
    mensaje = ""
    for i in range(n, 0, -1):
        mensaje += "*" * i + "\n"
    return mensaje

def mostrar_mensaje(mensaje):
    print(mensaje)

main()

#Ejercicio video IUTUB
MINIMO_VALOR= 0

def main():
    n= ingresar_entero_mayor_que("ingrese el valor de n", MINIMO_VALOR)
    dibujo = generar_dibujo(n)
    mostrar_mensaje(dibujo)



def ingresar_entero_mayor_que(mensaje,valor_minimo):
    repetir= True
    while repetir:
        valor=ingresar_entero(mensaje)
        if valor <= valor_minimo:
            print(f"el valor no es mayor que {valor_minimo}")
        else:
            repetir = False
    return valor



def generar_dibujo(n):
    dibujo = ""
    for j in range(0,n):
        dibujo += repetir_caracter("*",n-j)
        dibujo += repetir_caracter(".",2*j)
        dibujo += repetir_caracter("*",n-j) 
        dibujo += "\n"
    dibujo += repetir_caracter("*", 2*n)
    return dibujo

def repetir_caracter(caracter,cantidad):
    mensaje=""
    for i in range(0,cantidad):
        mensaje += caracter
    return mensaje


main()

#Ejercicio 3 

def main():
    inicio = ingresar_entero("Ingrese el número de inicio del rango: ")
    fin = ingresar_entero("Ingrese el número final del rango: ")
    suma = calcular_suma(inicio, fin)
    mensaje = generar_mensaje(inicio, fin, suma)
    mostrar_mensaje(mensaje)

def calcular_suma(inicio, fin):
    """Función para calcular la suma de los números dentro de un rango especificado."""
    suma = 0
    for i in range(inicio, fin + 1):
        suma += i
    return suma

def generar_mensaje(inicio, fin, suma):
    mensaje = f"La suma de los números desde {inicio} hasta {fin} es {suma}"
    return mensaje

def mostrar_mensaje(mensaje):
    print(mensaje)

main()
