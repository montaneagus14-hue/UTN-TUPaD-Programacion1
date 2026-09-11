saldo= 50000
dinero= 0

while True:

    print("""
    -CAJERO AUTOMATICO-

    1. Consultar saldo. 
    2. Ingresar dinero. 
    3. Retirar dinero. 
    4. Salir.
    """)


    opcion= input("Seleccione la opción (1 a 4): ")
    while not opcion.isdigit():
        print(" X Ingresó una opción incorrecta.")
        opcion= input("Vuelva a ingresar una opción entre 1 a 4: ")

    while int(opcion) >= 5:
        print("Ingresó un número que no está adentro de las opciones.")
        opcion= input(" X Vuelva a ingresar una opción entre 1 a 4: ")

        while not opcion.isdigit():
                print("Ingresó una opción inexistente.")
                opcion= input(" X Vuelva a ingresar una opción entre 1 a 4: ")

    match opcion: 
        case "1":
            print(f"Su saldo es de: ${saldo}")
        case "2":
            dinero= input("Ingrese la cantidad que desee ingresar: ")
            while not dinero.isdigit():
                print(" X No se pueden ingresar cantidades negativas o decimales.")
                dinero= input("Vuelva a ingresar la cantidad deseada: ")

            dinero= int(dinero)
            saldo= dinero + saldo

            print(f"Saldo actualizado: ${saldo}")

        case "3":
            dinero= input("Ingrese la cantidad que desee retirar: ")

            while not dinero.isdigit():
                print(" X No se pueden ingresar cantidades negativas.")
                dinero= input("Vuelva a ingresar la cantidad deseada: ")

            while int(dinero) > saldo:
                print(" X Fondos insuficientes")
                dinero= input("Vuelva a ingresar la cantidad deseada: ")

                while not dinero.isdigit():
                    print(" X No se pueden ingresar cantidades negativas.")
                    dinero= input("Vuelva a ingresar la cantidad deseada: ")

            dinero= int(dinero)
            saldo= saldo - dinero

            print(f"Saldo actualizado: ${saldo}")

        case "4":
            print(f"Su saldo quedo en: ${saldo}")
            print("Adiós")
            break
