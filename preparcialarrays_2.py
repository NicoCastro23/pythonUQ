def magia(lita_1, lista_2):
    lista_C = []
    for i in lita_1:
        for r in lista_2:
            if i == r:
                lista_C.append(lista_2)
    return lista_C
def generar_mensaje(dato):
    mensaje = f"los datos que se repien son {dato}"
    return generar_mensaje
mostrar_mensaje = lambda mensaje :print(mensaje)
def main():
    lista_A = ["Triangulo", "Circulo", "Cuadrado", "Rectangulo"]
    Lista_B = ["Triangulo", "Cuadrado"]
    hacer_proceso = magia(lista_A,Lista_B)
    generating_mensaje= generar_mensaje(hacer_proceso)
    mostrar_mensaje(generating_mensaje)
main()