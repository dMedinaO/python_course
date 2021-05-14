'''
previamente trabajamos con listas y ya sabemos como funcionan, a continuacion trabajaremos con un
nuevo tipo de listas que se llama Diccionario.

Practicamente los diccionarios son estructuras que permiten asociar una palabra clave a un valor,
este valor puede ser de cualquier tipo.
'''

#un diccionario se define entre llaves, las claves entre comillas seguido de : y el valor que representaran
dictionary = {"clave": 1, "clave2": "Valor 02", "clave3" : [1, 2, 3]}

#para acceder a un valor de un diccionario se hace con ['clave']
print(dictionary['clave2'])

#podemos obtener todas las claves existentes
print(dictionary.keys())

#podemos recorrer todas las claves usando estructuras for

for key in dictionary:
	print("Key {} tiene valor de {} ".format(key, dictionary[key]))

#podemos agregar elementos al diccionario
dictionary.update({"nueva_clave":["value1", "value2"]})

print(dictionary)

#NOTA: todas los ejemplos y demases vistos previamente pueden ser usados en diccionarios

#una clave, puede almacenar un diccionario tambien
dictionary_02 = {"clave_m" : 124}
dictionary.update({"dict_value":dictionary_02})
print(dictionary)

#Nota: el procesamiento de esto se llama Hash



