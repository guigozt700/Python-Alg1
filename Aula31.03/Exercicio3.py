def sePar(n):
    resto = n%2

    if resto == 0:
        return True
    else:
        return False
x = int(input('Numero: '))

if sePar(x):
    print('é par')
else:
    print('não é par')
