'''
los ciclos se refieren a estructuras repetitivas dentro de un segmento de codigo o acciones
que se necesiten se ejecuten un cierto numero de veces
En este ejemplo, se mostrara el uso de la estructura for, cuya funcion principal 
'''

numero_iteraciones = int(input("Ingrese el numero de iteraciones "))

#imprimiremos por pantalla un cierto numero de veces
for i in range(numero_iteraciones):#range permite determinar un rango, recibe dos numeros range(a,b) si a no existe, toma el valor de 0
	print("Impresion numero {}".format(i))

#tambien podemos hacer acciones dentro de un ciclo para mostrar un resultado por ejemplo, calcular una potencia
numero_base = int(input("Ingrese el numero base de la potencia "))
numero_exponente = int(input("Ingrese el exponente de la potencia "))

resultado_potencia = 1
for i in range(1, numero_exponente+1):#range toma su ultimo valor como el numero entregado menos 1
	resultado_potencia = resultado_potencia*numero_base

print("El resultado de {} elevado a {} es {}".format(numero_base, numero_exponente, resultado_potencia))

#finalmente pueden hacer operaciones mas complejas como los factoriales
numero_factorial = int(input("Ingrese el numero para obtener el factorial "))

resultado_factorial = 1

for i in range(1, numero_factorial+1):

	resultado_factorial = resultado_factorial*i

print("El factorial de {} es {}".format(numero_factorial, resultado_factorial))
