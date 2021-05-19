
my_dictionary = {"clave":1, "clave2":10}

print(my_dictionary)
print(my_dictionary['clave'])

for key in my_dictionary:
	print(my_dictionary[key])

mi_lista_vacia = []

number=1
cont=0

while cont<=10:

	if number%2 == 0:
		mi_lista_vacia.append(number)
		cont+=1

	number+=1

my_dictionary.update({"mi_lista":mi_lista_vacia})

print(my_dictionary)

mi_matriz = [[1,2,3],[4,5,6],[7,8,9]]

my_dictionary.update({"mi_matriz":mi_matriz})

print(my_dictionary)

my_dictionary.update({100:100})
print(my_dictionary)

my_dictionary_v2 = {"n1":"juanito perez", "n2": "pedrito carrasco"}
my_dictionary.update({"dict_data":my_dictionary_v2})

print(my_dictionary)

try:
	print(my_dictionary['mi_matriz_2'][3][1])
except:
	print("Key mi_matriz_2 no existe")
