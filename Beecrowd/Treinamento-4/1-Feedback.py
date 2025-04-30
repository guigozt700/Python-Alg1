diaTrabalho = int(input())

contTrabalho = 0

while contTrabalho < diaTrabalho:
    casosDia = int(input())

    contDia = 0
    nomes = ''

    while contDia < casosDia:
        feedBack = int(input())
        contDia += 1

        if feedBack == 1:
            nomes += 'Rolien\n'
        elif feedBack == 2:
            nomes += 'Naej\n'
        elif feedBack == 3:
            nomes += 'Elehcim\n'
        elif feedBack == 4:
            nomes += 'Odranoel\n'

    print(nomes, end='')

    contTrabalho += 1
