#numero primo se divide por 1 y por si mismo
numero_a_evaluar = int(input("Ingresa el numero a evaluar: "))

#opcion for
cont_divisores=0
start = 1

'''
for i in range(1, numero_a_evaluar+1):

	if numero_a_evaluar%i == 0:
		cont_divisores+=1

print("El numero de divisores para {} es {}".format(numero_a_evaluar, cont_divisores))

if cont_divisores ==2:
	print("El numero es primo")
else:
	print("El numero no es primo")
'''

flag = 0

while True:

	if numero_a_evaluar % start == 0:
		cont_divisores+=1

	if cont_divisores == 2:
		if numero_a_evaluar == start:
			flag=1
		break
	start+=1

if flag == 1:
	print("EL numero es primo")
else:
	print("El numero no es primo")
