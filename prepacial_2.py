
give_integer = lambda mensaje : int (input(mensaje))#lamda para fragmentar el codigo el cual nos permite ingresar un integer
show_message = lambda mensaje : print(mensaje)#lamda para fragmentar el codigo el cual nos da un show message
def loop_for(numero_uno, numero_dos):
    acumuler = 0
    for num in range(0, numero_dos):
        acumuler += numero_uno    
    show_message(acumuler)
            

    
while True:
    try:
        numero_uno = give_integer("Ingrese el límite inferior: ")
        numero_dos = give_integer("Ingrese el límite superior: ")
        
        
        
        show_message("El resultado seria")
        lopp_do = loop_for(numero_uno, numero_dos)
        print()
        
        break
    except ValueError:
        show_message("Error: Por favor ingrese valores enteros válidos. Intente de nuevo.")