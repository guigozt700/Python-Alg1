def exibeTabela(T, L, C):
    linha = 0
    while linha < L:  #percorre as linhas
        coluna = 0
        while coluna < C:    #percorre as colunas
            print(T[linha][coluna])
            coluna += 1
        print()
        linha += 1

def exibeTabela2(T,L,C):
    for linha in range(L):
        for coluna in range(C):
            print(T[linha][coluna])
        print()

def exibeTabela3(T):
    for linha in range(len(T)):
        for coluna in range(len(T[linha])):
            print(T[linha][coluna])
        print()


#        Tipo    Estoque  Preço   Importado
#         0         1       2         3
T = [['smartphone', 100, 1199.00, True], #0 
    ['televisão',   5, 2599.00, False ], #1
    ['notbook',      20, 4500.00, True]] #2

print('----- While -----')
exibeTabela(T,3,4)
print('----- For -----')
exibeTabela2(T,3,4)
print('----- Exibe 3 -----')
exibeTabela2(T,3,4)
