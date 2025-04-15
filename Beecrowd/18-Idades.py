soma = 0
cont = 0

idade = int(input())

while idade >= 0:
    soma += idade
    cont += 1
    idade = int(input())

print(f'{soma / cont:.2f}')
