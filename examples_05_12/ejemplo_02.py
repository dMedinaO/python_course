'''
Continuando con estructuras de ciclos, los for nos permitian ejecutar acciones limitadas a un valor fijo,
en este ejemplo trabajaremos con las estructuras while, quienes nos permiten ejecutar acciones hasta
que ocurra una condicion, es decir, no tenemos un numero de iteraciones fijas
'''

#ejemplo 01 -> trabajando con nombres
nombre = ""
while nombre != "Juan":
	nombre = input("Ingrese un nombre ")


#ejemplo 02 -> ingresar numeros hasta que sea par
is_par=False #los valores False y True, representan tipos de datos boolean

while not is_par: #los not permiten negar una afirmacion, cuando la condicion se declara sin ninguna data, se indica que es verdadero
	
	numero = int(input("Ingrese un numero a evaluar "))

	if numero%2 == 0:#esta es una forma de 
		print("El numero {} es par".format(numero))
		is_par=True
	else:
		print("El numero {} es impar".format(numero))
