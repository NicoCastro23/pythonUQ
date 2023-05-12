import apoyo as ap
mostrar_mensaje = lambda mensaje :print(mensaje)
def groso_troncos(cantidad):
    grosor = [0] * cantidad
    for i  in range (cantidad):
        grosor[i] = int(input("ingresar grosor"))
    return grosor
def seleccion_troncos(grosor_troncos):
    seleccion = []
    for i in grosor_troncos:
        if i >= 10 and i <= 14:
            agregar =seleccion.append(i)
    seleccion.sort
    return len(seleccion)
def generar_mensaje(mensaje):
    cantidad = f"hay {mensaje} troncos de 10-14 cm"
    return cantidad
def seleccion_troncos_mayor(grosor_troncos,tamaño):
    seleccion = []
    for i in grosor_troncos:
        if i >= 10 and i <= 14:
            agregar =seleccion.append(i)
    seleccion.sort()
    sicling = seleccion[tamaño-1]
    return sicling

def generar_mensaje_mayor(mensaje):
    mensaje = f"el numero mayor es {mensaje}"
    return mensaje

def main():
    cantidad_troncos = ap.ingresar_entero("cantidad de troncos")
    grosor_troncos = groso_troncos(cantidad_troncos)
    troncos_seleccionaos = seleccion_troncos(grosor_troncos)
    tronco_mayor =seleccion_troncos_mayor(grosor_troncos,troncos_seleccionaos)
    msj = generar_mensaje(troncos_seleccionaos)
    msj_2 = generar_mensaje_mayor(tronco_mayor)
    mostrar_mensaje(msj)
    mostrar_mensaje(msj_2)
main()