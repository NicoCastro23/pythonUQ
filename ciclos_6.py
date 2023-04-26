#Ejercicio 2

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