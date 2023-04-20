#Este programa pide un numero y da los multipos de 3 desde 6 hasta n donde n > 6
give_integer = lambda mensaje : int (input(mensaje))#lamda para fragmentar el codigo el cual nos permite ingresar un integer
show_message = lambda mensaje : print(mensaje)#lamda para fragmentar el codigo el cual nos da un show message
def ciclo_one(number):  #funcion que pide un number que va desde 6 -n
    for i in range (6,number):
        if condition_loop(i):#se llama la funcion condition tomando  a i que recorre el numero dado por el usuario 
            show_message(i)#se llama a show message

def condition_loop (ciclo):#conditional que nos permite dar los multiplos de 3 
    if ciclo % 3 == 0:
        return True
    else:
        return False
give_number = give_integer("ingrese un numero n:")# se llama la lamda que nos permite ingresar un numero
loop_do = ciclo_one(give_number)#se ejecuta el ciclo

    