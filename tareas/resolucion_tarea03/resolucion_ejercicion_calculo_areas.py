#Resolucion para ejercicio de calculo de areas, nos apoyaremos en un menu y la declaracion de funciones que faciliten el trabajo
import math#usar libreria de python

#funcion soporte para validar los datos de entrada, intenta la transformacion a float, retornando False o True cuando corresponda
def validated_input_data(input_data):

    response = True

    for value in input_data:
        try:
            value = float(value)
        except:
            response=False
            break
    
    return response

#Funciones de apoyo para el calculo de las areas de las figuras geometricas
def estimated_area_circulo(radio):
    return math.pi*float(radio)*float(radio)

def estimated_area_triangulo(base, altura):
    return float(base)*float(altura)/2

def estimated_area_rectangulo(ancho, largo):
    return float(ancho)*float(largo)

#funcion de apoyo para mostrar el menu
def print_menu():
    print(">>[1] Calcular area rectangulo")
    print(">>[2] Calcular area circulo")
    print(">>[3] Calcular area triangulo")
    print(">>[s/S] Salir")

#funciones de apoyo para obtener los datos de las figuras geometricas
def request_data_circle():
    radio_circle = input("Ingrese el radio del circulo\n>>")
    return [validated_input_data([radio_circle]), radio_circle]

def request_data_triangulo():
    base = input("Ingrese la base del triangulo\n>>")
    altura = input("Ingrese la altura del triangulo\n>>")
    return [validated_input_data([base, altura]), base, altura]

def request_data_rectangulo():
    ancho = input("Ingrese el ancho del rectangulo\n>>")
    alto = input("Ingrese el alto del rectangulo\n>>")
    return [validated_input_data([ancho, alto]), ancho, alto]

#funcion de apoyo que nos permite mostrar los datos por la pantalla
def print_output_formater(format_data, option_value):

    if option_value in ["1", "3"]:
        print("Con ancho {} y alto {} la figura {} tiene un area de {}".format(float(format_data[0]), float(format_data[1]), format_data[2], format_data[3]))
    else:
        print("Con radio {} la figura {} tiene un area de {}".format(float(format_data[0]), format_data[1], format_data[2]))

#funcion controlador, trabaja hasta que el usuario ingrese una s o S
def controller_process():

    while True:

        print_menu()#llamamos a la funcion que muestra el menu
        input_option = input(">>\n")

        if input_option == "1":
            response_data = request_data_rectangulo()#procesamos la data para estimar el area, esta funcion retorna una lista!
            if response_data[0]:
                area_rectangulo = estimated_area_rectangulo(response_data[1], response_data[2])#estimamos el area
                print_output_formater([response_data[1], response_data[2], "Rectangulo", area_rectangulo], input_option)#mostramos en formato
            else:
                print("Debe ingresar datos correctos para estimar el area de la figura seleccionada")
        
        elif input_option == "2":
            response_data = request_data_circle()
            if response_data[0]:
                area_circulo = estimated_area_circulo(response_data[1])
                print_output_formater([response_data[1], "Circulo", area_circulo], input_option)
            else:
                print("Debe ingresar datos correctos para estimar el area de la figura seleccionada")
        
        elif input_option == "3":
            response_data = request_data_triangulo()
            if response_data[0]:
                area_triangulo = estimated_area_triangulo(response_data[1], response_data[2])
                print_output_formater([response_data[1], response_data[2], "Triangulo", area_triangulo], input_option)
            else:
                print("Debe ingresar datos correctos para estimar el area de la figura seleccionada")
        elif input_option in ["s", "S"]:
            print("Gracias por preferirnos!")
            break
        else:
            print("La opcion ingresada no se encuentra en el menu, favor ingresar una nueva opcion")

#definimos la funcion principal del programa
def main():
    controller_process()#hacemos la llamada al controlador

#hacmos la llamada a la funcion principal
if __name__ == '__main__':
    main()
    