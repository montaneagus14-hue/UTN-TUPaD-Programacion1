
print("PANEL DE CONTROL")
print("Por favor ingresar la temperatura actual:")
print("(Para cerrar ingrese 'FIN')")
while True:
    temperatura= input("").strip().upper() 
    if temperatura == 'FIN':
        print("-Programa CERRADO-")
        break

    if temperatura == (''):
        print("ERROR")
        print("Se ha ingresado un valor vacío.")
        temperatura= input("Vuelva a intentarlo: (enter)")
        continue
    if temperatura == ".":
        print("ERROR")
        print("Se ha ingresado solo un punto '.'")
        temperatura= input("Vuelva a intentarlo: (enter)")
        continue

    digito_si= True 
    punto= 0

    for t in temperatura:
        if t == ".":
            punto += 1

        elif not t.isdigit():
            digito_si = False
            break

    if punto > 1 or not digito_si:
        print("Error")
        print("Se ha ingresado un valor inválido")
        temperatura= input("Vuelva a intentarlo: (enter)")
        continue

    temperatura= float(temperatura)

    if temperatura < 100.00 or temperatura > 500.00:
        print("¡ADVERTENCIA! Temperatura fuera de rango")

    print("TEMPERATURA REGISTRADA")


