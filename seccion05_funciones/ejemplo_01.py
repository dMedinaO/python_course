'''
Las funciones son metodos implementados por nosotros que cumplen cierta particularidad dentro del codigo
Las funciones se definen con la sentencia def

def mi_funcion (params):

	acciones
	return valor

mi_funcion -> nombre de la funcion que implementare y como se conocera dentro del script
params: -> son los parametros que recibe la funcion para trabajar, puede ser vacio y no recibir nada
return: -> expresion que indica que la funcion retornara una respuesta o no

Ejemplificaremos todo esto generando una calculadora que permita sumar, restar, multiplicar y dividir, para ello
implementaremos una funcion para cada operacion, con las validaciones correspondientes, De manera adicional
contemplaremos la generacion de un menu y la evaluacion de las opciones, este script correra hasta que el
usuario pulse la opcion finalizar
'''

#ejemplo de una funcion que no recibe parametros y retorna la opcion ingresada por el usuario
def show_menu():

	print("Opciones de calcula:")
	print(">>1: Sumar")
	print(">>2: Restar")
	print(">>3: Multiplicar")
	print(">>4: Dividir")
	print(">>5: Salir")

	return input(">> ")

def capture_data():

	numero1 = int(input("Ingrese el primer numero "))
	numero2 = int(input("Ingrese el segundo numero "))

	return numero1, numero2#podemos retornar diferentes variables a la vez, separados por una coma

def sumar(numero1, numero2):
	return numero1+numero2

def restar(numero1, numero2):
	return numero1-numero2

def multiplicar(numero1, numero2):
	return numero1*numero2

def dividir(numero1, numero2):

	#los try/except representan manejos de excepciones dentro de un bloque de codigo peligroso, ejemplos de 
	#esto corresponden a divisiones por 0, acceder a una variable nula, acceder a un indice o key en una lista
	#hash que no exista, etc.

	try:
		return numero1/numero2#dentro del try se intenta ejecutar el codigo, si no puede, salta de inmediato al except
	except:
		return "Error"

#funcion que tendra el control de las acciones
def control_calculadora():

	while True:#esta linea representa "Siempre verdadero", aprenderemos a forzar su quiebre

		opcion_ingresada = show_menu()#de esta forma se llaman a funciones que retornan algo

		#efectuamos la validacion de las opciones
		if opcion_ingresada == "1":
			print("Realizar suma")
			numero1, numero2 = capture_data()
			respuesta = sumar(numero1, numero2)
			print("{} + {} = {}".format(numero1, numero2, respuesta))

		elif opcion_ingresada == "2":
			print("Realizar resta")
			numero1, numero2 = capture_data()
			respuesta = restar(numero1, numero2)
			print("{} - {} = {}".format(numero1, numero2, respuesta))

		elif opcion_ingresada == "3":
			print("Realizar multiplicacion")
			numero1, numero2 = capture_data()
			respuesta = multiplicar(numero1, numero2)
			print("{} x {} = {}".format(numero1, numero2, respuesta))

		elif opcion_ingresada == "4":
			print("Realizar Division")
			numero1, numero2 = capture_data()
			respuesta = dividir(numero1, numero2)

			if respuesta == "Error":
				print("No es posible division {} y {}, intente otros numeros".format(numero1, numero2))
			else:
				print("{} / {} = {}".format(numero1, numero2, respuesta))

		elif opcion_ingresada == "5":
			print("Finalizando calculadora")
			break#como su traduccion al espanol, rompe el ciclo

		else:
			print("Debe ingresar una opcion valida")

#la funcion main representa la funcion de control del script, normalmente se encuentra implicita. Pero, comenzaremos
#a utilizarla
def main():

	control_calculadora()

if __name__ == '__main__':
	main()


