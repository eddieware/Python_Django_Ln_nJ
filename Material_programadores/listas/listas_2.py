print("Dime alguna asignatura para crear la lista y presiona 'f' para salir")
lista = []
palabra = ''

while palabra != 'f':  # mientras palabra es diferente de f se hace
    palabra = input()  # palabra igual a entrada
    lista += [palabra]  # la lista crece incrementalmente agregando lo que se introduce por palabra
    print("dime otra asignatura o presiona 'f' para salir")
lista.pop()  # quitamos el caracter f de la lista

for i in (lista):  # for en [0 1 2]
    print("yo estudio : ", i)  # imprime con cada elemento de la lista
