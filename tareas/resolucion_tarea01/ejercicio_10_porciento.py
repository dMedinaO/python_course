#resolucion ejercicio 10%

#recepcion de variables inputs
monto_afp = float(input("Ingrese el monto a retirar asociado al 10% "))
valor_dolar_actual = float(input("Ingrese el valor del dolar "))
habilitados_aeropuertos = int(input("Los aeropuertos estan habilitados? <1> Si, <2> No "))
estan_vacunados = int(input("Se encuentran ambos vacunados? <1> Si, <2> No "))

#procesamiento, hacemos las transformaciones
total_valor = monto_afp/valor_dolar_actual
print("Usted tiene un total de {} USD para viajar ".format(total_valor))

if total_valor > 7500:
    print("Se cumple con el criterio del monto!")

    if estan_vacunados == 1:
        print("Ambos se encuentran vacunados!")

        if habilitados_aeropuertos == 1:
            print("Aeropuertos habilitados, condiciones necesarias para viajar")
        elif habilitados_aeropuertos == 2:
            print("Los aeropuertos no se encuentran habilitados, no se puede viajar")
        
        else:
            print("Solo se permite ingresar un valor entre 1 y 2")
    
    elif estan_vacunados == 2:
        print("Deben estar ambos vacunados, no pueden viajar")
    
    else:
        print("Solo se permite ingresar un valor entre 1 y 2")

else:
    print("El monto no es suficiente para hacer el viaje. Lo sentimos!")
