def impar(n):
    return n%2 == 1
    
n = int(input('Numero: '))

if impar(n):
    print('Impar!')
else:
    print('Par!')
