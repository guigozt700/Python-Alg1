def geraLista(v, qtd):
    L = [v] #Inicia a lista com o valor digitado = L[0]

    for i in range(1, qtd): #Começa em L[1] porque a posição L[0] é o valor
        # Inicio L[1]: Para acessar a posição L[0], diminui 1 (L[i-1]) e depois o loop vai aumentando corretamente
        L.append(2 * L[i-1])
    return L

def exibirLista(L, qtd):
    i = 0
    while i < qtd:
        print(f'N[{i}] = {L[i]}') #Indice e valor
        i += 1

def main():
    valor = int(input())
    lista = geraLista(valor,10) #Passa o valor e o tamanho da lista para gerar
    exibirLista(lista, 10)
    
main()
