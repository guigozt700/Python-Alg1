casos = int(input())

lista = []

for _ in range(casos):
    num = int(input())

    somaDiv = 0

    for i in range(1, num):
        if num % i == 0:
            somaDiv += i

    if somaDiv == num:
        lista.append(f'{num} eh perfeito')
    else:
        lista.append(f'{num} nao eh perfeito')

for imprime in lista:
    print(imprime)
