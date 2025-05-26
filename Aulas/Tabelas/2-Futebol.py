def exibeTabela(T,L,C):
    for linha in range(L):
        for coluna in range(C):
            print(T[linha][coluna])
        print()

def preencheTabela(T, L, campos):
    for linha in range(L):
        registro = []
        for campo, tipo in campos:
            x = tipo(input(f'{campo}:'))
            registro.append(x)
        print('-' * 30)
        T.append(registro)

def main():
    T = []
    campos = [('time',      str),
              ('pontuacao', int),
              ('qtdJogos',  int),
              ('vitorias',  int),
              ('derrotas',  int),
              ('empates',   int)]
    preencheTabela(T, 3, campos)
    exibeTabela(T, len(T), len(T[0]))


main()

