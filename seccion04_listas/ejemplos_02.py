'''
Previamente, trabajamos con listas, las cuales representan elementos ordenados
En este ejemplo veremos las listas de listas, es decir, estructuras que permiten almacenar listas
dentro de su data, los ejemplos mas conocidos, son las matrices, pero, se aplica a toda data que tenga
la caracteristica de "doble", "triple" u otros
'''

import random

lista = [1,2,3]

matriz = []

for i in range(3):
	matriz.append(lista)

print(matriz)

#si accedemos a un indice, obtendremos una lista
print(matriz[1])

#si queremos acceder a un elemento especifico, ocupamos dobles indices
print(matriz[1][1])#el primero hace referencia al indice de la fila, mientras que el segundo al indice de la columna

#para verlo de mejor manera
for i in range(len(matriz)):
	print("Accediendo a fila: {}".format(i))

	for j in range(len(matriz[i])):
		print("Accediendo a columna {}".format(j))
		print("El elemento es: ", matriz[i][j])

#se pueden hacer operaciones con las matrices como sumar, restar o multiplicar
matrix_ampliada = []

for i in range(len(matriz)):
	row_data = []

	for j in range(len(matriz[i])):
		random_value = random.randint(0,9)
		value_add = matriz[i][j]*random_value
		row_data.append(value_add)
	matrix_ampliada.append(row_data)


#otra manera de hacer un for es la siguiente
for row in matrix_ampliada:#al hacerlo de esta forma, se indice que row va tomando cada elemento en matriz ampliada
	print(row)