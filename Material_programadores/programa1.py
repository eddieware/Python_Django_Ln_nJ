from datetime import datetime

#minutos_magicos = [2, 4, 6, 8, 10 , 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]

#minuto_actual = datetime.today().minute
#modificar el programa para trabajar con segundos
#modificar el programa para que se repita 30 veces
#para que espere un segundo entre cada repeticion

#
# if minuto_actual in minutos_magicos:
#    print("Minuto Magico!!!!")
#    if minuto_actual == 18:
#            print("son 18 minutos")
# else:
#    print("No es Minuto Magico")

#El operador in nos ayuda a verificar si una cosa esta contenida
#dentro de la otra

# minutos_magicos = [2, 4, 6, 8, 10 , 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]

# minuto_actual = datetime.today().minute
# modificar el programa para trabajar con segundos
# modificar el programa para que se repita 30 veces
# para que espere un segundo entre cada repeticion


# if minuto_actual in minutos_magicos:
#    print("Minuto Magico!!!!")
#    if minuto_actual == 18:
#            print("son 18 minutos")
# else:
#    print("No es Minuto Magico")

# El operador in nos ayuda a verificar si una cosa esta contenida
# dentro de la otra


##################################Actividad###############################


segundos_magicos = [2, 4, 6, 8, 10 , 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]


# modificar el programa para trabajar con segundos
# modificar el programa para que se repita 30 veces
# para que espere un segundo entre cada repeticion




# El operador in nos ayuda a verificar si una cosa esta contenida
# dentro de la otra

i = 1


while i < 30:
    segundo_actual = datetime.today().second

    if i == segundo_actual:
        print(i)
        i = i+1
    else:
        print("Incrementando")
        print(i)



    # if segundo_actual in segundos_magicos:
    #     print("Segundo Magico!!!!")
    #
    #
    # else:
    #     print("No es Segundo Magico")
    #     i = i + 1
    #     print(i)




    #
    #
    #     print(i)
    #     i += 1
    #
    #
    #
    #     print("No es Segundo Magico")
    #     print(i)






