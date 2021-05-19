def suma_dos_numeros(num1, num2):
	resultado = num1+num2
	return resultado

def resta_dos_numeros(num1, num2):
	resultado = num1-num2
	return resultado

def multiplica_dos_numeros(num1, num2):
	resultado = num1*num2
	return resultado

def dividir_dos_numeros(num1, num2):
	
	try:
		resultado = num1/num2
		return resultado
	except:
		return "error"

def print_menu():

	print("[1] Suma dos numeros")
	print("[2] Resta dos numeros")
	print("[3] Multiplica dos numeros")
	print("[4] Divide dos numeros")
	print("[-1] Para salir")

def get_numeros_by_standard_input():

	number_01 = int(input(">> "))
	number_02 = int(input(">> "))

	return number_01, number_02

while True:

	print_menu()

	try:
		input_option = int(input("Ingrese su opcion "))

		if input_option == 1:
			print("Suma")
			number_01, number_02 = get_numeros_by_standard_input()
			resultado = suma_dos_numeros(number_01, number_02)
			print("{} + {} = {}".format(number_01, number_02, resultado))

		elif input_option == 2:
			print("Restar")
			number_01, number_02 = get_numeros_by_standard_input()
			resultado = resta_dos_numeros(number_01, number_02)
			print("{} - {} = {}".format(number_01, number_02, resultado))

		elif input_option == 3:
			print("Multiplica")
			number_01, number_02 = get_numeros_by_standard_input()
			resultado = multiplica_dos_numeros(number_01, number_02)
			print("{} x {} = {}".format(number_01, number_02, resultado))

		elif input_option == 4:
			print("Divide")
			number_01, number_02 = get_numeros_by_standard_input()
			resultado = dividir_dos_numeros(number_01, number_02)
			print("{} / {} = {}".format(number_01, number_02, resultado))

		elif input_option == -1:
			print("Adios!")
			break
		else:
			print("Seleccione una opcion correcta")

	except:
		print("Solo ingresar numeros")