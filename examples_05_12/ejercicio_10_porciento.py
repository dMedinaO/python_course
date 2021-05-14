'''
@Author: juanito Perez
@mailto: juanito.perez@mail.com

entrada = 7500 USD
dolar = 720 

aeropuerto_chile = SI/NO, 0, 1, True, False
aeropuerto_francia = SI/NO
total_AFP = ZZZ
estan_vacunados = SI/NO

necesitaba = 7500*720
'''

aeropuerto_chile = input("Esta habilitado el aeropuerto de Chile? <Si>, <NO>").upper()
aeropuerto_francia = input("Esta habilitado el aeropuerto de Francia? <Si>, <NO>").upper()
estan_vacunados = input("Pedro y su novia estan vacunados? <Si>, <NO>").upper()
monto_retiro = int(input("Ingrese el monto del retiro "))

if aeropuerto_chile == "SI" and aeropuerto_francia == "SI":
	if estan_vacunados == "SI":
		if monto_retiro > 7500:
			print("OK, viaja")
		else:
			print("El monto es menor a 7500 USD")
	else:
		print("No se encuentran vacunados")
else:
	print("Los aeropuertos no estan activos")


