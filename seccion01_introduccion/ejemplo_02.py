'''
En este ejemplo, podemos recibir las variables desde la entrada estandar, efectuando una interaccion
con el usuario, para ello nos apoyaremos de la funcion input()
'''

variable_ejemplo = input("Ingrese cualquier cosa ")#con input podemos almacenar en una variable cualquier cosa

print(variable_ejemplo)

#usando un cast puedes definir la variable con el tipo que tu necesites
variable_ejemplo = float(input("Ingrese un numero: "))
print("Numero ingresado {}".format(variable_ejemplo))
