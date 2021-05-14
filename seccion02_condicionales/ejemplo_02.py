'''
Al aplicar condiciones, estas se pueden mezclar, por ejemplo, preguntar por rangos de numeros o cosas
de estilo similar. Ademas, tambien pueden hacer condiciones dentro de condiciones, por ejemplo si pasa X preguntar
si pasa Z, lo cual se conoce como condiciones anidadas
'''

import sys #leer variables desde la linea de comando

#leer desde la linea de comando
temperatura = float(input("Ingrese la temperatura "))
pbb_lluvia = float(input("Ingrese la pbb de lluvia "))

#comienzo de decisiones
if temperatura > 30:
	print("Debo usar polera y shorts")

else:
	if temperatura <=30 and temperatura >=20:
		print("Debo usar polera y jeans")

	else:

		if temperatura <20 and temperatura >=10:
			print("Debo usar polera, jeans y camisa")

		else:
			print("Debo usar parka y jeans")

#condiciones de pbb de lluvia
if pbb_lluvia >50:
	print("Debo llevar paraguas")