
give_integer = lambda mensaje : int (input(mensaje))#lamda para fragmentar el codigo el cual nos permite ingresar un integer
show_message = lambda mensaje : print(mensaje)#lamda para fragmentar el codigo el cual nos da un show message
show_message_two = lambda mensaje, mensaje_dos : print(mensaje, mensaje_dos)#lamda para fragmentar el codigo el cual nos da un show message
def condition_limit(limite_superior, limite_inferior):
    if limite_superior <= limite_inferior:
        show_message("El límite superior debe ser mayor al límite inferior. Intente de nuevo.")
        return show_message, True
    else:
        return False
    
def condition_tree(num):
    
    if num % 3 == 0:
            return  True
    else:
         return False
    
def loop_for(limite_inferior, limite_superior):
    contador_multiplos_tres = 0
    for num in range(limite_inferior, limite_superior + 1):
            show_message(num)
            if condition_tree(num ):
                contador_multiplos_tres += 1
                show_message("- múltiplo de tres")

    show_message_two("Cantidad de múltiplos de tres identificados:", contador_multiplos_tres)

while True:
    try:
        limite_inferior = give_integer("Ingrese el límite inferior: ")
        limite_superior = give_integer("Ingrese el límite superior: ")
        if condition_limit(limite_superior, limite_inferior):
            continue
        
        
        show_message("Listado de números entre")
        lopp_do = loop_for(limite_inferior, limite_superior)
        print()
        
        break
    except ValueError:
        show_message("Error: Por favor ingrese valores enteros válidos. Intente de nuevo.")


        

