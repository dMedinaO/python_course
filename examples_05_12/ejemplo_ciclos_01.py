
total_numeros = int(input("Ingrese el total de numeros a evaluar "))
inicio = int(input("Ingrese el numero del cual quiero partir "))

contador_pares = 0
'''
for i in range(inicio, total_numeros-1):
	print(i)
	if i%2 == 0:
		print("{} es par".format(i))
		contador_pares = contador_pares+1
		#contador_pares+=1 -> contador_pares++
'''
while contador_pares <= total_numeros:
	print("Evaluando valor {}".format(inicio))

	if inicio%2 == 0:
		print("{} es par".format(inicio))
		contador_pares = contador_pares+1

	inicio+=1

	
	