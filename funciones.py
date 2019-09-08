def pedir_pizza():
    print("Estoy pidiendo una pizza")


def checar_entrada(edad):

    if edad < 18:
        print("NO puedes entrar")
    elif edad >= 21:
        print("puedes entrar y tambien puedes beber")
    else:
        print("puedes entrar al bar pero no puedes beber")

edad = 21
edad_2 = 17
checar_entrada(edad_2)
