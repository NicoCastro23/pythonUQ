#Ejercicio 2
"""
def main():
    frase= ingresar_cadena("ingrese una frase:")
    proceso= determinar_cantidad_vocales(frase)
    resto= generar_mensaje(proceso)
    mostrar_mensaje(resto)
def ingresar_cadena(cantidad):
    valor= input(cantidad)
    return valor
def determinar_cantidad_vocales(letra):
    vocal_a = 0
    vocal_e = 0
    vocal_i = 0
    vocal_o = 0
    vocal_u = 0
    for letra in letra:
        if letra == "a":
            vocal_a += 1
        elif letra == "e":
            vocal_e += 1
        elif letra == "i":
            vocal_i += 1
        elif letra == "o":
            vocal_o += 1
        elif letra == "u":
            vocal_u += 1
    cantidad= (vocal_a,vocal_e,vocal_i,vocal_o,vocal_u)
    return cantidad
def generar_mensaje(resto):
    mensaje = ""
    vocales = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(vocales)):
        mensaje += f"La vocal {vocales[i]} aparece {resto[i]} veces\n"
    return mensaje
    
def mostrar_mensaje(resto):
    print(resto)
main()
"""

#Ejercicio 3
def main():
    frase = ingresar_cadena("Ingrese una frase: ")
    frase_sin_vocales = eliminar_vocales(frase)
    mensaje_sin_vocales = generar_mensaje_sin_vocales(frase_sin_vocales)
    mostrar_mensaje(mensaje_sin_vocales)

def ingresar_cadena(mensaje):
    valor = input(mensaje)
    return valor

def eliminar_vocales(frase):
    nueva_frase = ""
    for letra in frase:
        if letra.lower() not in "aeiou":
            nueva_frase += letra
    return nueva_frase

def generar_mensaje_sin_vocales(frase_sin_vocales):
    mensaje = "La frase sin vocales es:\n"
    mensaje += f"{frase_sin_vocales}\n"
    return mensaje

def mostrar_mensaje(mensaje):
    print(mensaje)


main()
