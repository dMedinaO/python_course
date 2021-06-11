'''
1 ->Si las letras corresponden de A a D con mayúsculas y minúsculas, emplee un número random entre 1 y 10.
    Opciones de interpretacion:
        - Las mayusculas y minusculas pueden tener diferentes valores!
        - Mayusculas y minusculas deben tener mismo valor
2 ->Si las letras corresponden de E a K, emplee un número random entre 10 y 100, en el caso de que la letra sea mayúscula, debe multiplicarlo por -1.

3 ->Finalmente, si representa un número, debe reemplazarla por la letra en su posición en el abecedario.
'''
import random
import string

def encoding_first_statment(character, dictionary_data):

    if character not in dictionary_data:
        dictionary_encoding.update({character:random.randrange(1,10)})
    return dictionary_encoding

def encoding_second_statment(character, dictionary_data):

    if character not in dictionary_data:
        response_encode = random.randrange(1,100)
        if character.isupper():
            response_encode = response_encode*-1
        dictionary_encoding.update({character:response_encode})
    return dictionary_data

#example string to encoding
string_variable_encode = "Debo ir a comprar al supermercado en silencio. Matias no sabe La Existencia de las GaLLetas en el PISO 50 de los AlfaJORes"

#creamos el abecedario
abecedario_mayus =string.ascii_uppercase

#diccionario que guardara todas nuestras claves
dictionary_encoding = {}
dictionary_decoding = {}
#procesamos todos los caracteres
for character in string_variable_encode:
    if character in ["A", "B", "C", "D", "a", "b", "c", "d"]:
        dictionary_encoding = encoding_first_statment(character, dictionary_encoding)
    elif character in ["E", "F", "G", "H", "I", "J", "K", "e", "f", "g", "h", "i", "j", "k"]:
        dictionary_encoding = encoding_second_statment(character, dictionary_encoding)
    
    elif character.isnumeric():
        if character not in dictionary_encoding:
            dictionary_encoding.update({character:abecedario_mayus[int(character)]})
    else:
        dictionary_encoding.update({character:character})
        
encoding_message = ""
for character in string_variable_encode:
    encoding_message+=str(dictionary_encoding[character])        

print(encoding_message)