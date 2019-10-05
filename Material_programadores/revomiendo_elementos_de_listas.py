# numeros=[1,2,3,4,5,6]
#
# numeros.remove(2)
#
# print(numeros)
#METODO POP!!!!!!!!!!!!!!!!!!!
# numeros = [1,2,3,4,5]
# numeros.pop(1)
#METODO EXTEND PARA AGREGAR ELEMENTSO A LA LISTA
#numeros = [1,2,3,4,5]
# numeros_20=[6,7,8,9,11,12,13,14,15,16,17,18,19,20]
# numeros.extend(numeros_20)
# print
numeros = [1,2,3,4,5]
#numeros.insert(0,2)# insert es para insertar un caracter en una posicion


#numeros2 = numeros.copy()# para devolver una referencia de la lista existente mas no una copia
#print(numeros2)
# len(numeros)

###############################################
letras = list("perro")
print(letras)

numeros2 = list(range(20))
print(numeros2)

for numero in numeros[::1]:
    print(numero)