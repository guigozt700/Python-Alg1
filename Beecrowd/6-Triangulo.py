a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
print('Triangulo', end = ' ')

if a == b and b == c:
    print('Equilatero')
else:
    if a == b or b == c or a == c:
        print('Isódceles')
    else:
        print('Escaleno')
