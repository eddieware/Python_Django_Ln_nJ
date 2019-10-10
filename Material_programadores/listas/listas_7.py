letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y','z']
listanuevanumeros=[]
listanuevapalabras=[]
Sizeletras = len(letras)

############
#listanumeros = list(enumerate(letras, 1))
# print(range(,Sizeletras+1))
listanumeros2=list(range(1, Sizeletras + 1))
#print(listanumeros2)
#print("DIVISION")
#print(letras)


for n in range(len(letras)):
    #print ("letras :",letras[n],"numeros", listanumeros2[n])
    operacion=listanumeros2[n]/3
    parte_entera = int(operacion)
    parte_decimal = abs(operacion) - abs(int(operacion))
    #print("parte entera: ",parte_entera,"parte decimal: ",parte_decimal)
    if(parte_decimal==0):
      listanuevanumeros+=[listanumeros2[n]]
      listanuevapalabras+=[letras[n]]
      #print("paso una vez")
#print(listanuevanumeros,"\n",listanuevapalabras)
print(letras)
for n in listanuevapalabras:
    letras.remove(n)
print(letras)

# en n se almancena cada elemento de la lista y se va removiendo con la funcion en el for


