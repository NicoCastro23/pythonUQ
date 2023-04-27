#taller
#Este programa nos permite leer cunatos digitos tiene un numero
give_string = lambda mensaje : str (input(mensaje))#lamda para fragmentar el codigo el cual nos permite ingresar un string

give_number = give_string ("digite el numero:")#se llama al lamda give string

contar = len (give_number)#se utiliza el metodo len para leer number 
print (contar)#se imprime contar