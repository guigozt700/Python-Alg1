numA = int(input('Digite o numero 1: '))
numB = int(input('Digite o numero 2: '))

divInteira = numA - (numA // numB * numB)

print(divInteira)

if(divInteira == numA):
    print('divisivel')
else:
    print('não divisivel')

