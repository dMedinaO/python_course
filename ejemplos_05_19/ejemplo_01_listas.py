
mi_primera_lista = [1, 4, 10, "Perro", 2.56]
print(mi_primera_lista)

#indices en python nos permiten acceder a los contenidos de la lista

print(mi_primera_lista[3])
print(mi_primera_lista[-2])

for i in range(len(mi_primera_lista)):
	print("El valor de la lista en la posicion {} es {}".format(i, mi_primera_lista[i]))

mi_lista_vacia = []

number=1
cont=0

while cont<=10:

	if number%2 == 0:
		mi_lista_vacia.append(number)
		cont+=1

	number+=1

print(mi_lista_vacia)


suma_lista = mi_primera_lista + mi_lista_vacia
print(suma_lista)

suma_lista[5] = "nuevo valor"
print(suma_lista)