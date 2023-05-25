ingresar_entero = lambda mensaje :int(input(mensaje))
def definir(cantidad):
    valores =[""]* cantidad
    for i in range(cantidad):
        valores[i] = str(input("ingrese un nombre:"))
    return valores

def filtrar(lista):
    lista_nueva = []
    for i in lista:
        if i.startswith("j"):
            lista_nueva.append(i)
    return lista_nueva

def generar_mensaje(dato):
    mensaje = f"los nombres que empiezan con j son: {dato}"
    return mensaje
mostrar_mensaje = lambda mensaje :print(mensaje)

def main():
    ingresar_numero = ingresar_entero("ingresar numero de estudiantes:")
    ingresar_lista = definir(ingresar_numero)
    mensaje = generar_mensaje(ingresar_lista)
    mostrar_mensaje(mensaje)
main()


