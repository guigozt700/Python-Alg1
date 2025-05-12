def preencher(L):
    for i in range(10):
        x = int(input())
        L[i] = x

def transforma(L):
    i = 0
    while i < 10:
        if L[i] <= 0:
            L[i] = 1
        i += 1

def exibe(L):
    for i in range(len(L)):
        print(f'X[{i}] = {L[i]}')

def main():
    L = 10 * [0] # cria uma lista com 10 posições com 0 [0,0,0...]
    preencher(L)
    transforma(L)
    exibe(L)

main()
