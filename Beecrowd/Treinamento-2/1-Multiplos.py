def multiplos(a,b):
    if a % b == 0 or b % a == 0:
        return 'Sao Multiplos'
    else:
        return 'Nao sao Multiplos'

a, b = input().split()
a, b = int(a), int(b)

print(multiplos(a,b))
