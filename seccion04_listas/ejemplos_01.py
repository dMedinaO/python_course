'''
Las listas son estructuras de datos que permiten almacenar elementos ordenados y que pueden ser accedidos por indices
estas pueden ser de 1 dimension a N dimensiones, dependiendo de la data que se quiere almacenar
'''

lista = [2,4,"Juan"]#las listas se declaran con [] y los elementos internos se separan por ,

print("Largo de la lista {} ".format(len(lista)))#el metodo len nos permite acceder al largo de la lista

numero_elementos = 10
diff = numero_elementos - len(lista)
#agregaremos elementos hasta que el largo sea 10
for i in range(diff):
	value = input("Ingrese un valor ")
	lista.append(value)#con el metodo append pueden ingresar registros a una lista

print(lista)

#para acceder a un elemento de una lista, lo pueden hacer por su indice, los indices SIEMPRE parten en 0
print("Indice 1: ", lista[1])
print("Indice 3: ", lista[3])

#python acepta indices negativos, los cuales toman el valor en orden inverso
print("Indice -1: ", lista[-1])
print("Indice -2: ", lista[-2])

#existe una forma mas eficiente: usando ciclos
for i in range(len(lista)):
	print("Elemento en indice {} tiene el valor de {}".format(i, lista[i]))

#otras operaciones de las listas consisten en formar sub listas o conjuntos de ellas
sub_lista = lista[1:4]#con un rango especifico
sub_lista2 = lista[:2]#desde el inicio hasta un indice determinado
sub_lista3 = lista[2:]#desde un indice determinado hasta el fin de la lista

print(lista)
print(sub_lista)
print(sub_lista2)
print(sub_lista3)

#NOTA: todo lo que se ha visto previamente, se puede aplucar a listas

#NOTA 02: los str o palabras son listas de caracteres
variable_str = "Hola nuevo mundo"

for i in range(len(variable_str)):
	print("Character: {}".format(variable_str[i]))