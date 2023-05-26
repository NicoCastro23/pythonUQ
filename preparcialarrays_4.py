#Un grupo de estadística de la universidad del
#Quindío requiere recolectar unos datos de un grupo de estudiantes de ingeniería de
#sistemas y computación, entre esos datos esta el nombre del estudiante, el género y la
#edad , para ello requiere un programa que le permita capturar esta información y
#adicionalmente totalizar cuantas personas son de género masculino, cuántas personas
#de género femenino, cuántos superan la mayoría de edad, cuál es el promedio de edad
#de las personas de género masculino y cuál es el nombre de la persona de género
#femenino de menor edad, indicar el nombre y la edad de esa persona.
ingresar_entero = lambda mensaje :int(input(mensaje))
def definir(cantidad):
    valores =[""]* cantidad
    for i in range(cantidad):
        valores[i] = str(input("ingrese un nombre:"))
    return valores
def generar_mensaje(dato):
    mensaje = f"los nombres que empiezan con j son: {dato}"
    return mensaje
mostrar_mensaje = lambda mensaje :print(mensaje)

def main():
 pass
main()