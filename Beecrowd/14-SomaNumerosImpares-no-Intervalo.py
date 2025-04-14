numMin = int(input())
numMax = int(input())

indice = numMin + 1
soma = 0

while indice < numMax:
    if indice % 2 != 0:
        soma += indice
    indice += 1

print(soma)
        
