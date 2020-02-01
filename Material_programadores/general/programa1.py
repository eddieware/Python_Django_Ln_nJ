from datetime import datetime
import time
segundos_magicos = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]



for i in range (30):
    segundo_actual = datetime.today().second

    if segundo_actual in segundos_magicos:
        print("es segundo magico")

    else:
        print("no es segundo magico")

    time.sleep(1)

