'''
Al igual que las condiciones se pueden anidar, los ciclos tambien, ejemplos clasicos son el trabajo con matrices
datos en formato tabla, series de tiempo doble, dobles sumatorias, expresiones matematicas, etc.

En este script se mostraran algunos ejemplos clasicos
'''

#Imprimiendo un cuadrado de *
filas = int(input("Ingrese el numero de filas "))
columnas = int(input("Ingrese el numero de columnas "))

for i in range(filas):
	fila_imprimir = ""
	for j in range(columnas):
		fila_imprimir+="*"
	print(fila_imprimir)

#imprimiendo una piramide de *
alto = int(input("Ingrese el alto de la piramide "))

for i in range(alto):
	row = "*"

	for j in range(i):
		row+="*"
	print(row)



