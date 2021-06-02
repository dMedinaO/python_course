#resolucion ejercicios factoriales

#se desarrollara mediante ciclo infinito para trabajar y practicar con ciclos y validar los ingresos
while True:
    
    input_data = input("Ingrese el numero a estimar el factorial, ingrese -1 para finalizar ")
    print("Valor ingresado: {}".format(input_data))

    #condicion de termino
    if input_data == "-1":
        print("Termino del programa!")
        break
    else:#condicion de termino no se cumple, continua la ejecucion
        try:#intentamos la transformacion a numero
            value_to_estimate = int(input_data)

            if value_to_estimate >=0:#validamos que solo sean numericos

                print("Obteniendo el numero factorial...")

                resultado = 1

                for i in range(1, value_to_estimate+1):
                    resultado = resultado*i
                
                print("{}! = {}".format(value_to_estimate, resultado))
            else:
                print("Debes ingresar un numero entero mayor o igual a 0")

        except:#mostramos mensaje de error
            print("Debes ingresar un numero valido")

    

