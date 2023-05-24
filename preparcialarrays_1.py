def proceso(lista):
    lista_c = []
    for i in lista:
        if i % 3 != 0:
            lista_c.append(i)
    return lista_c

def generar_mensaje(dato):
    mensaje = f"los datos que no son multiplos son: {dato}"
    return mensaje

mostrar_mensaje = lambda mensaje :print(mensaje)

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    hacer = proceso(lista)
    mensaje = proceso(hacer)
    mostrar_mensaje(mensaje)
main()