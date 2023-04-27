def main ():
 valor1 = ingrese_real ("ingrese valor inferior: ")
 valor2 = ingrese_real ("ingrese valor superior: ")
 process = calculo_ciclo (valor1, valor2)
 process2 = calculo_multiplos (valor1, valor2)
 print (process2 and process)

def ingrese_real (mensaje):
  numero = int (input (mensaje))
  return numero

def calculo_ciclo (inferior, superior):
  while True: 
   try:
       
       if  inferior >= superior:
          print ("el valor inferior debe ser menor al superior, intentelo de nuevo.")
          continue
       
      
   except ValueError:
      print ("ingrese de nuevo un numero entero...")


def calculo_multiplos (inferior, superior):
  multiplos = 0
  for num in range (inferior,superior+1):
    if num % 3 == 0:
       print (num,"es multiplo de 3")
       multiplos += 1
    else:
       print (num)

print (f"la cantidad de multiplos de tres encontrados es de:")

main ()