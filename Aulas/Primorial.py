from math import sqrt, ceil

def primorial(n):
    result = 2              #vai iniciar a contagem do for (ex:2*3)
    raiz = ceil(sqrt(n))    #guardao resultado da raiz quadrada (arredondando pra cima)

    for pd in range(3, raiz, 2): #pd vai percorrer de 3 até a raiz, pulando de 2 em 2
        result *= pd

        if result == n:
            return True
    return False

def main():
    num = int(input())

    if primorial(num):
        print ('S')
    else:
        print('N')

main()
