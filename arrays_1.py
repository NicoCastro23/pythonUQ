mensaje = lambda mensaje, mensaje2, mensaje3, mensaje4 : print(mensaje, mensaje2, mensaje3, mensaje4)
def definir():
    cantidad = int(input("definir cantidad:"))
    valores =[0.0]* cantidad
    for i in range(cantidad):
        valores[i] = float(input("ingrese un numero:"))
    return valores
def condition(nota):
    condicion = True
    if nota >= 3.0:
        return condicion
    else:
        return not condicion
def condition_2(n):
    condicion = True
    if n <= 3.0:
        return condicion
    else:
        return not condicion
def loop (n):
    ganados = 0
    perdidos = 0 
    for notas in n:
        if condition(notas):
            ganados += 1
        elif condition_2(notas):
            perdidos +=1
        mensaje("ganaron:", ganados,"perdieron:", perdidos)  

def main():
    deinifir_estudiantes = definir()
    lop_do = loop(deinifir_estudiantes)
main()
#saber promedio, saber not max y nota min