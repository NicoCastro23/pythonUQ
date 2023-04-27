#Sofía, una estudiante de matemáticas necesita un programa que le ayude a imprimir un
#listado de números enteros entre dos valores indicados por ella. Además quiere que por
#cada número del intervalo el programa indique si es o no múltiplo de tres. Al final del
#listado, el programa indicará la cantidad de múltiplos identificados.(puta sofia)
give_integer = lambda mensaje : int (input(mensaje))#lamda para fragmentar el codigo el cual nos permite ingresar un integer
show_message = lambda mensaje : print(mensaje)#lamda para fragmentar el codigo el cual nos da un show message
show_message_two = lambda mensaje, mensaje_dos : print(mensaje, mensaje_dos)#lamda para fragmentar el codigo el cual nos da un show message
def condition_limit(limite_superior, limite_inferior):# se declara condicion para obligar al proframa a obtener un numero mayor
    if limite_superior <= limite_inferior:
        show_message("El límite superior debe ser mayor al límite inferior. Intente de nuevo.")
        return show_message, True
    else:
        return False
    
def condition_tree(num):#condicion para encontrar los multiplos
    
    if num % 3 == 0:
            return  True
    else:
         return False
    
def loop_for(limite_inferior, limite_superior):#bucle para recorrer los numeors
    contador_multiplos_tres = 0
    for num in range(limite_inferior, limite_superior + 1):
            show_message(num)
            if condition_tree(num ):# se llama la condicion para encontrar multiplos
                contador_multiplos_tres += 1
                show_message("- múltiplo de tres")

    show_message_two("Cantidad de múltiplos de tres identificados:", contador_multiplos_tres)

while True:
    try:
        limite_inferior = give_integer("Ingrese el límite inferior: ")
        limite_superior = give_integer("Ingrese el límite superior: ")
        if condition_limit(limite_superior, limite_inferior):#se llama la condicio para obligar numeros mayores
            continue
        
        
        show_message("Listado de números entre")
        lopp_do = loop_for(limite_inferior, limite_superior)#se llama al loop con la condicion adentro
        print()
        
        break
    except ValueError:
        show_message("Error: Por favor ingrese valores enteros válidos. Intente de nuevo.")


        

