'''
En este ejemplo, puedes recibir variables desde la linea de comando, es decir, al momento de ejecutar el script
esto es, cuando se ejecuta python3 script.py, se reciben los parametros que uno desee:
python3 script.py ejemplo01 ejemplo02 ejemplo03

El control de estos parametros lo genera la libreria sys con las variables argv, argv representa una lista, es decir
un conjunto ordenado de elementos representados por una variable (se vera en detalle en el ejemplo de listas)
'''

import sys#con la palabra reservada import, indican que ocuparan funciones de python previamente implementadas

#procesamos las variables de argumentos/parametros
variables = sys.argv

#podemos imprimir las listas
print(variables)

#importante las listas se ven de esta forma: [a, b, c, d], donde cada elemento se define en una posicion y para acceder a ellos
#se debe indicar la posicion, siempre con un numero menos, asi, si quiero leer la letra a en este caso que esta en la posicion 1
#debo indicarlo con el indice 0,

#NOTA: en argv, siempre el primer elemento es el nombre del programa, por definicion
print(variables[1])
print(variables[2])

#tu tambien puedes castear las variables para que funcionen con el tipo de dato que necesites
variable1 = int(variables[1])
variable2 = float(variables[2])



