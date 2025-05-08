def divisao(x, y):
    q = 0
    
    while x >= y:
        x -= y
        q += 1
    print(f'Quociente = {q}')

x = int(input())
y = int(input())

divisao(x, y)
