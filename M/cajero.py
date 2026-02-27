saldo = float(input("Digite su saldo: "))
opcion = ""
while opcion != "3":
    try: 
        opcion = input("Que desea hacer 1=Retirar - 2=Depositar - 3=Salir ")
        if opcion == "1":
            ret = float(input("¿Cuanto desea retirar?: "))
            if ret > saldo:
                print("Saldo insuficiente")       
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
        print("El dato ingresado NO es valido")
