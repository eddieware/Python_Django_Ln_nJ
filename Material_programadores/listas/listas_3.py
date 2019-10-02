asignatura = []
nota = []
palabra = ''

while palabra != 'f':  # mientras palabra es diferente de f se hace
    print("Dime la asignatura y la nota o presiona 'f' para salir")

    palabra = input()  # palabra igual a entrada
    if palabra != 'f':
        # print("Dime La asignatura")
        asignatura += [palabra]  # la lista crece incrementalmente agregando lo que se introduce por palabra
        print("Dime La nota obtenida")
        palabra = input()
        nota += [palabra]
    else:
        print("programa terminado")

# asignatura.pop()#quitamos el caracter f de la lista

# print(nota, asignatura)

for i in range(len(nota)):
    print("yo estudio: ", asignatura[i], "y obtuve : ", nota[i])

# for i in (asignatura): # for en [0 1 2]


# num = (1,2,3,4,5)
# letr = ("a", "b", "c", "d", "e")
# for n in range(len(num)):
# print num[n], letr[n]