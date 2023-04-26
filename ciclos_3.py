#Con este codigo se utiliza para multiplicar 2 numeros sin necesidad de *
number = lambda mensaje : int(input(mensaje))#lamda para fragmentar el codigo el cual nos permite ingresar un integer
show_message = lambda mensaje : print(mensaje)#lamda para fragmentar el codigo el cual nos da un show message
def ciclo_multiplicacion(numer_one, number_two):#funcion de loop
    z = 0#se declara z fuera de la variable
    for i in range(0, number_two):#un loop donde se va desde el cero hasta e numeor 2 
        z += numer_one # 3+3+3+ #z sirve como acumulador 
        show_message(z)#se llama a show mwssage
        
give_number = number("numero 1:") #se declara numero 1
give_number_two = number("numero 2:") # se declara numero 2
ejecute_loop = ciclo_multiplicacion(give_number, give_number_two)#se llama todo e codigo
