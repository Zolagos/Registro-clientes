saldo_cuenta1 = 0
saldo_cuenta2 = 0
cuenta_actual = 1
CUATROPMIL = 0.004
opcion = ""
while opcion != "4":
    try: 
        print(f"""
Tu saldo en cuenta 1 es: {saldo_cuenta1}
Tu saldo en cuenta 2 es: {saldo_cuenta2}
Actualmente te encuentras en la cuenta {cuenta_actual}
        """)

        opcion = input("\nQue desea hacer\n 1=Retirar\n 2=Depositar\n 3=Cambiar de cuenta\n 4=Salir\n")

        if cuenta_actual == 1:
            saldo = saldo_cuenta1
        else:
            saldo = saldo_cuenta2
            
        if opcion == "1":

            ret = float(input("¿Cuanto desea retirar?: "))

            saldo_total = saldo_cuenta1 + saldo_cuenta2
            ret_4 = ret + (ret*CUATROPMIL)

            if ret > saldo_total:
                print("No tienes dinero suficiente en ambas cuentas")
                continue

            if ret_4 > saldo_total:
                print("debido al 4x100 no tienes dinero suficiente en ambas cuentas")
                continue

            if ret_4 > saldo:
                
                print(f"el saldo de la cuenta {cuenta_actual} no es suficiente, se completara con la otra cuenta")
                
                if cuenta_actual == 1:
                    saldo_cuenta2 = saldo_cuenta2 - (ret_4 - saldo)
                else:
                    saldo_cuenta1 = saldo_cuenta1 - (ret_4 - saldo)    

                saldo = 0
            else:
                saldo =  saldo - ret_4
                
            print(f"Nuevo saldo de la cuenta {cuenta_actual} es: {saldo}")

            if cuenta_actual == 1:
                saldo_cuenta1 = saldo
            else:
                saldo_cuenta2 = saldo

        elif opcion == "2":
            dep = float(input("¿Cuanto desea hacer de deposito?: "))
            if dep < 0:
                print("Dato invalido")
            else:
                saldo = saldo + dep
                print(f"Nuevo saldo de la cuenta {cuenta_actual} es: {saldo}")

            if cuenta_actual == 1:
                saldo_cuenta1 = saldo
            else:
                saldo_cuenta2 = saldo

        elif opcion == "3":
            if cuenta_actual == 1:
                cuenta_actual = 2
            else:
                cuenta_actual = 1
        elif opcion == "4":
            print("Saliendo")
    except:
        print("El dato ingresado NO es valido\n")
