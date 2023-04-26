
def main():
  value = ingrese_real ("ingrese el valor a sumar: ")
  process = procedimiento_suma (value)
  mensaje = generar_mensaje (process)
  mostrar = mostrar_mensaje (mensaje)

main()

generar_mensaje = lambda mensaje : print(mensaje)


def ingrese_real (mens):
    valor = int(input(mens))
    return valor

def  procedimiento_suma (valor):
  valor = int (valor[0]) + int(valor[1]) + int(valor[2]) + int(valor[3])
  return valor
show_message = lambda mensaje : print(mensaje)#lamda para fragmentar el codigo el cual nos da un show message