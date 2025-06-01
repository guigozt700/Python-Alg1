def geraLista(qtd):
    L = []
    for i in range(qtd):
        L.append(int(input()))
    return L

def troca(L,i,j):
    aux = L[i]
    L[i] = L[j]
    L[j] = aux

def inverte(L,qtd):
    i = 0
    j = qtd-1
    while i < j:
        troca(L,i,j)
        i += 1
        j -= 1

def exibeLista(L,qtd):
     for i in range(qtd):
         print(f'N[{i}] = {L[i]}')
         

def main():
    L = geraLista(5)
    inverte(L,5)
    exibeLista(L,5)

main()

 
