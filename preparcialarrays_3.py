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
def filtrar_nombres_por_letra(lista_nombres):
    nombres_filtrados = []
    for nombre in lista_nombres:
        if isinstance(nombre, str) and nombre.startswith("j"):
            nombres_filtrados.append(nombre)
    return nombres_filtrados
def main():
    ingresar_numero = ingresar_entero("ingresar numero de estudiantes:")
    ingresar_lista = definir(ingresar_numero)
    filtar_lista = filtrar_nombres_por_letra(ingresar_lista)
    mensaje = generar_mensaje(filtar_lista)
    mostrar_mensaje(mensaje)
main()



