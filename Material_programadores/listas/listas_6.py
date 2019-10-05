asignaturas = []
notas = []
passed=[]
palabra = ''


while palabra != 'f':
    print("Dime la asignatura y la nota o presiona 'f' para salir")

    palabra = input()  # palabra igual a entrada
    if palabra != 'f':

        asignaturas += [palabra]  # la lista crece incrementalmente agregando lo que se introduce por palabra
        print("Dime La nota obtenida de 1 a 10")
        palabra = input()
        notas += [palabra]

    else:
        print("programa terminado")

print(asignaturas, notas)
SizeArray = len(asignaturas)

for n in range(len(notas)):
    print ("En la asignatura :",asignaturas[n],"obtuviste", notas[n])

    # remarkfinal