import sys
import math

primer_numero = int(input("Ingrese el primer numero "))
segundo_numero = int(input("Ingrese el segundo numero "))
operacion = int(input("Ingrese la operacion que desea "))

if operacion == 1:

	print("Vamos a sumar")
	resultado = primer_numero+segundo_numero
	print(resultado)

elif operacion == 2:
	print("Vamos a restar")
	resultado = primer_numero - segundo_numero
	print(resultado)

elif operacion == 3:
	print("Vamos a Multiplicar")
	resultado = primer_numero * segundo_numero
	print(resultado)

elif operacion == 4:
	
	print("Vamos Dividir")
	resultado = primer_numero / segundo_numero
	print(resultado)

elif operacion == 5:

	print("Vamos a obtener porcentaje")
	resultado = segundo_numero*100/primer_numero
	print(resultado)

elif operacion == 6:
	print("Vamos a sacar potencias")
	resultado = math.pow(primer_numero, segundo_numero)
	print(resultado)

else:
	print("No hay ningua opcion valida")
