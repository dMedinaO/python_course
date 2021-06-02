#resolucion ejercicios contaminacion ambiental

#recepcion de variables
ppm_data = float(input("Ingrese el valor de las PPM "))
habitantes_ciudad = float(input("Ingrese el total de habitantes en MM "))

#procesamos las condiciones y mostramos los mensajes
if ppm_data >=10:
    print("Zona en alerta Negra")
    print("Aviso de alerta de seguridad a la comunidad")

elif ppm_data >=7 and ppm_data <10:
    print("Zona en alerta Roja")

    if habitantes_ciudad >=5:
        print("Aviso de alerta de seguridad a la comunidad")

elif ppm_data >=4 and ppm_data <7:
    print("Zona en alerta Naranja")

    if habitantes_ciudad >=7:
        print("Aviso de alerta de seguridad a la comunidad")


elif ppm_data >=2 and ppm_data <4:
    print("Zona en alerta Amarilla")

else:
    print("No se declara alerta")