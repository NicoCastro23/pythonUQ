while True:
    try:
        limite_inferior = int(input("Ingrese el límite inferior: "))
        limite_superior = int(input("Ingrese el límite superior: "))
        if limite_superior <= limite_inferior:
            print("El límite superior debe ser mayor al límite inferior. Intente de nuevo.")
            continue
        contador_multiplos_tres = 0
        print("Listado de números entre", limite_inferior, "y", limite_superior, ":")
        for num in range(limite_inferior, limite_superior + 1):
            print(num, end=" ")
            if num % 3 == 0:
                print("- múltiplo de tres", end=" ")
                contador_multiplos_tres += 1
            print()
        print("Cantidad de múltiplos de tres identificados:", contador_multiplos_tres)
        break
    except ValueError:
        print("Error: Por favor ingrese valores enteros válidos. Intente de nuevo.")


        

