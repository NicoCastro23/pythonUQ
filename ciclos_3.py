number = lambda mensaje : int(input(mensaje))
show_message = lambda mensaje : f"{mensaje}"
def ciclo_multiplicacion(numer_one, number_two):
    z = 0
    for i in range(0, number_two):
        z += numer_one # 3+3+3+3
        return show_message(z)
give_number = number("numero 1:") # 3
give_number_two = number("numero 2:") # 4
ejecute_loop = ciclo_multiplicacion(give_number, give_number_two)
print(ejecute_loop)

