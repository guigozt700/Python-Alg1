from time import sleep

while True:
    hora = 24

    while hora >+ 0: #3 - quando a hora chegar em 23
        minuto = 60

        while minuto >= 0: #2 - quando os minutos chegar em 59
            segundo = 60
            
            while segundo >= 0: #1 - quando os segundos chegar em 59
                print(f'{hora:02}:{minuto:02}:{segundo:02}') #formatação onde o 0 vai ocupar o lugar a esquerda (01, 02...)
                segundo -= 1
            minuto -= 1
        hora -= 1
