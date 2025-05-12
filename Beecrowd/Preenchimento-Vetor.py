
def geraLista(v, qtd):
    L = [v]

    for i in range(1,qtd):
        L.append(2* L[i-1])
    return L

def exibeLista(L, qtd):
    i = 0
    while i < qtd:
        print(f'N[{i}] = {L[i]}')
        i += 1

def main():
    v = int(input())
    L = geraLista(v,10)

    exibeLista(L,10)

main()
