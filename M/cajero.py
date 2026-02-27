saldo = 0
opcion = ""
while opcion != "3":
    try: 
        print("Tu saldo es: ",saldo)
        opcion = input("\nQue desea hacer\n 1=Retirar\n 2=Depositar\n 3=Salir\n")
        if opcion == "1":
            ret = float(input("¿Cuanto desea retirar?: "))
            if ret > saldo:
                print("Saldo insuficiente\n")       
            else:
                saldo =  saldo - ret
                print(f"Nuevo saldo es: {saldo}")
        elif opcion == "2":
            dep = float(input("¿Cuanto desea hacer de deposito?: "))
            if dep < 0:
                print("Dato invalido")
            else:
                saldo = saldo + dep
                print(f"Nuevo saldo es: {saldo}")
        elif opcion == "3":
            print("Saliendo")
    except:
        print("El dato ingresado NO es valido\n")
