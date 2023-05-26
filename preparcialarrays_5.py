#Una función que reciba un arreglo de palabras y un carácter, y retorne
#las posiciones donde las palabras empiezan por ese caracter
ingresar_entero = lambda mensaje :int(input(mensaje))
ingresar_string = lambda mensaje :str(input(mensaje))
def definir(cantidad):
    valores =[""]* cantidad
    for i in range(cantidad):
        valores[i] = str(input("ingrese una palabra:"))
    return valores

def generar_mensaje(dato, letra):
    mensaje = f"los nombres que empiezan con {letra} son: {dato}"
    return mensaje

mostrar_mensaje = lambda mensaje :print(mensaje)

def filtrar_nombres_por_letra(lista_nombres, letra):
    nombres_filtrados = []
    for nombre in lista_nombres:
        if isinstance(nombre, str) and nombre.startswith(letra):
            nombres_filtrados.append(nombre)
    return nombres_filtrados
def main():
    ingresar_numero = ingresar_entero("ingresar numero de palabras:")
    ingresar_lista = definir(ingresar_numero)
    ingresar_letra = ingresar_string("defina la letra:")
    filtar_lista = filtrar_nombres_por_letra(ingresar_lista, ingresar_letra)
    mensaje = generar_mensaje(filtar_lista, ingresar_letra)
    mostrar_mensaje(mensaje)
main()

