preciototal= 0

while True: 

    if preciototal == 0:
        print("""
""")
        print("~FAST FOOD~")
        print("""
Bienvenido CAJERO al servicio de Fast Food
Por favor cargar la opción del CLIENTE:
""")
        
    else:
        print("")
        print("Continuar pedido:")
    
    print("""    1. Agregar Hamburguesa ($4500) 
    2. Agregar Papas Fritas ($2000) 
    3. Agregar Bebida ($1500) 
    4. Pagar el pedido (Cierra el ticket) 
    5. Cancelar pedido y salir 
    """)

    opcion= input("  → ")
    while not opcion.isdigit():
            print("X Opción incorrecta")
            print("Volver a ingresar opción entre 1 a 5")
            opcion= input("  → ")

    while int(opcion) >= 6:
        print("X Número ingresado fuera de las opciones.")
        print("Volver a ingresar opción entre 1 a 5")
        opcion= input("  → ")

        while not opcion.isdigit():
                    print("X Opción incorrecta")
                    print("Volver a ingresar opción entre 1 a 5")
                    opcion= input("  → ")

    print("")
    print(f"(Opción seleccionada {opcion})")
    print("")

    match opcion: 
        case "1": 
            precio= 4500
            preciototal += precio
            print(f">Hamburguesa agregada. Total actual: ${preciototal}")
        case "2":
            precio= 2000
            preciototal += precio
            print(f">Papas Fritas agregadas. Total actual: ${preciototal}")
        case "3":
            precio= 1500
            preciototal += precio
            print(f">Bebida agregada. Total actual: ${preciototal}")
        case "4":
            print("Pedido listo para pagar")
            print("============================")
            print("Ticket cerrado")
            print("TOTAL:")
            print(f"${preciototal}")
            print("============================")

            print("(Metodo de pago 'efectivo')")
            dinero= input("Cantidad de dinero con la que el cliente pagará: \n$")

            while not dinero.isdigit():
                print("X Incorrecto")
                print("El Valor no corresponde a una suma de dinero.")
                dinero= input("Volver a ingresar: \n$")

            while int(dinero) < preciototal:
                print("X Incorrecto")
                print("Dinero ingresado menor al precio total.")
                print(f"-Total a abonar: \n${preciototal} ")
                dinero= input("Volver a ingresar: \n$")

                while not dinero.isdigit():
                                print("X Incorrecto")
                                print("El valor no corresponde a una suma de dinero.")
                                dinero= input("Volver a ingresar: \n$")

            print("============================")
            print("Dinero ingresado correctamente.")
            print(f"Efectivo: ${dinero}")

            vuelto= int(dinero) - preciototal

            print(f"Cambio a entregar: ${vuelto:.2f}")
            print("-Pedido realizado-")
            print("============================")
        
            preciototal= 0 
        case "5":
            print("[Pedido CANCELADO]")
            print("Adiós")
            break