a = int(input('ladoA: '))
b = int(input('ladoB: '))
c = int(input('ladoC: '))

if a < b+c and b < a+c and c < a+b:
    print('Tringulo perfeito!')
else:
    print('Não é triangulo!')
