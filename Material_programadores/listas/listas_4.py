#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
num_loteria=[]
palabra = ''

while palabra != 'f':  # mientras palabra es diferente de f se hace
    print("Dime algun numero ganador de la loteria o presiona 'f' para salir")
    palabra = input()  # palabra igual a entrada
    if palabra != 'f':

        num_loteria += [palabra]  # la lista crece incrementalmente agregando lo que se introduce por palabra

    else:
        print("programa terminado")
num_loteria.sort(reverse=True)
print("los numeros ganadores son: ",num_loteria)

