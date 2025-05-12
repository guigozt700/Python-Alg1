def mentirinha(n):
    qtdDivisores = 0

    for pd in range(1, n+1):
        if n % pd == 0:
            qtdDivisores += 1
            
    return qtdDivisores == 3

n = int(input())

if mentirinha(n):
    print('sim')
else:
    print('nao')
