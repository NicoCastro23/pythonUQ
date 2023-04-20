give_number = lambda mensaje: int (input(mensaje))#lamda para fragmentar el codigo el cual nos permite ingresar un integer
show_message = lambda mensaje : print(mensaje)#lamda para fragmentar el codigo el cual nos da un show message
def ciclo_counter(numero):#creacion de una funcion con un lopp
    acumuler = 0#se declara el acumulador
    while numero > 0 :#condicion
        acumuler += 1 #el acumulador 
        numero = numero // 10 #esta es la clave de codigo por cada vez que se repita el codigo se divide en 10 pero entero
        show_message(acumuler)#se llama al lamda y se muestra el acumuler

number = give_number ("dar un numero:")#se llama al give number
do_loop = ciclo_counter(number)# se llama a ciclo