def criaMatriz(L, C):
    """
    L = quantidade de Linhas.
    C = quantidade de Colunas
    """
    M = []
    for i in range(L):
        linha = C * [0.0]
        M.append(linha)
    return M

def preenche(M, L, C):
    """
    M = matriz que será preenchida
    L = quantidade de linha
    C = quantidade de colunas
    """
    for i in range(L):
        for j in range(C):
            M[i][j] = float(input())

def resultado(operacao, M, L, C):
    soma = 0
    for i in range(C):
        soma += M[L][i]

    if operacao == 'S':
        return soma
    else:
        return soma / C

def main():
    linhaOperacao = int(input())
    operacao = intput()

    M = criaMatriz(12, 12)
    preenche(M, 12, 12)
    resp = resultado(operacao, M, 12, 12)

    print(f'{resp:.1f}')

main()
