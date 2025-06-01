def geraLista(qtd):
    A = []
    for i in range(qtd):
        A.append(float(input()))
    return A

def exibeLista(A):
    for i in range(len(A)):
        if A[i] <= 100:
            print(f'A[{i}] = {A[i]:.1f}')

def main():
    A = geraLista(100)
    exibeLista(A)
    
main()
