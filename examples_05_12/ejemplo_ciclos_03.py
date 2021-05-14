'''
Trabajaremos resolviendo una sumatoria en espacio X,Y

Sum i=1:n sum j=1:k (j*i)/(j+i)
'''

n = int(input("Ingrese el tope de N "))
k = int(input("Ingrese el tope de k "))

resultado = 0

for i in range(1, n+1):
	for j in range(1, k+1):
		resultado = resultado + (j*i)/(j+i)

print("El valor de la sumatoria es: {}".format(resultado))

