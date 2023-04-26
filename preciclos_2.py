
def main():
  value = ingrese_real ("ingrese el valor a sumar: ")
  process = procedimiento_suma (value)
  mensaje = generar_mensaje (process)
  mostrar = mostrar_mensaje (mensaje)

def  procedimiento_suma (valor):
  valor = int (valor[0]) + int(valor[1]) + int(valor[2])
  return valor
mostrar_mensaje = lambda mensaje : print(mensaje)#lamda para fragmentar el codigo el cual nos da un show message
generar_mensaje = lambda mensaje : print(mensaje)
ingrese_real = lambda mensaje : int(input(mensaje))