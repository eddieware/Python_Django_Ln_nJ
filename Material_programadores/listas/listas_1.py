print("Dime alguna asignatura para crear la lista y presiona 'f' para salir")
lista=[]
palabra=''

while palabra != 'f':
    palabra = input()
    lista+=[palabra]
    print("dime otra palabra o presiona 'f' para salir")
carrier=(len(lista))
lista.pop()
print("Las asignaturas son : " , lista)