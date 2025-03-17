numA = int(input('Numero A: '))
numB = int(input('Numero B: '))
numC = int(input('Numero C: '))

print('Maior numero: ', end='')

if numA > numB and numA > numC:
    print(numA)
else:
    if numB > numA and numB > numC:
        print(numB)
    else:
        print(numC)
