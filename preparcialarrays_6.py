#Una función que dado un numero entero, retorne un arreglo o lista donde
#en cada posición se encuentre un digito del numero, se debe almacenar en forma
#invertida. Ejemplo si el numero es 12345 debe retornar un arreglo o lista de la
#siguiente manera {5,4,3,2,1}
ingresar_entero = lambda mensaje :str(input(mensaje))

def generar_mensaje(dato):
    mensaje = f"la lista invertida es: {dato}"
    return mensaje
def ejecutar_ciclo(numero):
    nueva_lista =[]
    for i in numero:
        nueva_lista.append(i)
    nueva_lista.reverse()
    return nueva_lista
mostrar_mensaje = lambda mensaje :print(mensaje)

def main():
    ingresar_numero = ingresar_entero("ingrese el numero:")
    invertir_numero = ejecutar_ciclo(ingresar_numero)
    generating_message = generar_mensaje(invertir_numero)
    mostrar_mensaje(generating_message)
main()