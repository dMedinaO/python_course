#resolucion ejercicios figuras

altura = int(input("Ingrese la altura de la piramide "))
caracter = input("Ingrese el caracter a utilizar ")
option_print = int(input("Ingrese el tipo de piramide a realizar\n<1> Izqquierda a derecha creciente\n<2> Izqquierda a derecha decreciente\n<3> Derecha  a Izquierda con base final\n<4> Derecha a izquierda con base inicial "))

if option_print == 1:
    print("opcion 01 izquierda a derecha con base creciente")

    #opcion 01 izquierda a derecha con base creciente
    for i in range(altura+1):
        row = caracter*i
        print(row)

elif option_print == 2:
    print("opcion 02 izquierda a derecha con base decreciente")
    #opcion 02 izquierda a derecha con base decreciente
    for k in range(altura, 0, -1):
        row = "*"*k
        print(row)

elif option_print == 3:
    print("opcion 03 derecha a izquierda con base creciente")
    #opcion 03 derecha a izquierda con base creciente
    for i in range(altura):
        row = ""
        for j in range(altura-i):
            row = row + " "
        
        for j in range(i+1):
            row = row+caracter
        
        print(row)

else:
    print("opcion 04 derecha a izquierda con base decreciente")
    #opcion 04 derecha a izquierda con base decreciente
    for i in range(altura):
        row = ""
        
        for j in range(i+1):
            row = row+" "
        
        for j in range(altura-i):
            row = row +caracter
        
        print(row)