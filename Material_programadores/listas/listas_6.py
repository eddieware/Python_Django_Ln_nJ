subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
#La idea principal aqui es relacionar la subject con la nota en cada interacion asi n1 va con m1
for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    if score >= 5:# Si la nota es mayor a 5
        passed.append(subject)# se agregan las pasadas a passed
        print(subject)
for subject in passed:#Se recorre subject en passed, subject siene los elementos separados y passed la lista
    subjects.remove(subject)# sew remueve
print("Tienes que repetir " + str(subjects))# se imprime
