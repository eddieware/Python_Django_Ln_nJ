vocales=['a','e','i','o','u']
palabra='mama'
vocales_encontradas=[]
for ch in palabra:
    if ch in vocales:
        if ch not in vocales_encontradas:
            vocales_encontradas.append(ch)# append es para añadir a la lista las vocales encontradas a la lista
for vocal in vocales_encontradas:
    print(vocal)