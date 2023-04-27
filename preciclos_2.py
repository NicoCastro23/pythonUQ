#Sofía quiere completar el programa anterior para que por cada número del listado, muestre
#la operación con sus dígitos, para este caso la suma, además, del resultado obtenido al
#sumarlos. Por ejemplo, si el número fuera 19234, la operación a mostrar sería 1 + 9 + 2 + 3
#+ 4 y su resultado daría 19.(sofia es una lok)
generar_mensaje = lambda mensaje : print(mensaje)#lamda para fragmentar el codigo el cual nos da un show message
ingrese_real = lambda mensaje : str(input(mensaje))#lamda para ingresar un numero que se alamcana como una str

def  procedimiento_suma (valor):#Proceso el cual hara sicling con el numeor dado y cada unmero lo convertira en ineteger para posteriormente sumarlo
  valor = int (valor[0]) + int (valor[1]) + int (valor[2]) + int (valor[3])
  return valor

def main ():
  value = ingrese_real ("ingrese el valor a sumar: ")
  process = procedimiento_suma (value)
  mensaje = generar_mensaje (process)
main()