generar_mensaje = lambda mensaje : print(mensaje)#lamda para fragmentar el codigo el cual nos da un show message

ingrese_real = lambda mensaje : str(input(mensaje))

def  procedimiento_suma (valor):
  valor = int (valor[0]) + int (valor[1]) + int (valor[2]) + int (valor[3])
  return valor


value = ingrese_real ("ingrese el valor a sumar: ")
process = procedimiento_suma (value)
mensaje = generar_mensaje (process)


