#Ejercicios complementarios de listas
#crear una programa que guarde una lista de palabras el programa debe pedir el numero de palabras
#luego solicitar ese numero de palabras y luego mostrarlas

print("escribe el numero de palabras que quieras guardar")
numero_palabras=int(input())
if numero_palabras < 1:
    print("inserta un numero valido")
else:
    lista=[]
    #i el elemento que podemos cambiar, rango de numero de palabras para hacer rango n
    for i in range (numero_palabras):
        print("dime la palabra", str(i+1) + ": ")
        # si imprimes un str no puedes imprimir un int en la misma linea por eso se hace la suma i+1 y luego de convierte a str

        palabra = input()
        lista+=[palabra]
    print("La lista creada es : " , lista)