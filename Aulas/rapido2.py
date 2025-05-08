from math import ceil, sqrt

def primo(n):
    if n % 2 == 0: return n == 2
    raiz = ceil(sqrt(n))
    
    for pd in range(3,raiz+1, 2):
        if n % pd == 0:
            return False
    return True

def main():
    casos = int(input())
    result = ''

    for i in range(casos):  
        n = int(input())

        if primo(n):
            result += 'Prime\n'
        else:
            result += 'Not Prime\n'
            
    print(result, end='')


main()
