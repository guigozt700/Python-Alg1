#Versão ingênua

def exibe(L, n):
    for posicao, item in enumerate(L[ : n]): 
        print(f'N[{posicao}] = {item}')

def preenche(L, n, t):
    x = 0
    
    for i in range(n): 
        L[i] = x 
        x += 1

        if x == t:
            x = 0

def main():
    
    t = int(input())
    tamanho = 1000
    L = tamanho * [0]
    
    preenche(L, tamanho, t)
    exibe(L, tamanho)

main()
