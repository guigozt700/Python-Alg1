def misterio(x,y):
    x *= 2
    z = y

    while x > 1:
        y = z // 2

        while y >= 1:
            print(x + y)
            y -= 1
            
        z //= 2
        x -= 1
    return

a = int(input())
b = int(input())

misterio(a,b)

print('Prova facil')
