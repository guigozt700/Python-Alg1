from time import sleep

minuto = 0

while minuto < 60:
    segundo = 0
    
    while segundo < 60:
        print(f'00:{minuto:02}:{segundo:02}') #formatação onde o 0 vai ocupar o lugar a esquerda (01, 02...)
        segundo += 1
        #sleep(0.2)
    minuto += 1
