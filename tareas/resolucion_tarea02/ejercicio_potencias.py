#resolucion ejercicios de potencias

#misma logica que en el ejercicio de los factoriales
while True:#ciclo infinito

    input_data = input("Pulse -1 para salir, cualquier otra opcion para continuar ")

    if input_data == "-1":#condicion de ciclo
        print("Termino del programa")
        break
    
    else:#iniciamos el proceso

        try:#intentamos transformar

            potencia = int(input("Ingrese el valor de la potencia "))
            exponente = int(input("Ingrese el valor del exponente "))
            print("Potencia {} y exponente {}".format(potencia, exponente))

            #validamos ambos sean positivos
            if exponente >0 and potencia >0:
                resultado = 1

                for i in range(exponente):
                    resultado = resultado*potencia
                    
                print("{} elevado a {} es {}".format(potencia, exponente, resultado))
            else:
                print("Ingresar por favor numeros positivos mayores a 0")

        except:#manejamos el error
            print("Error, ingresa valores correctos")
