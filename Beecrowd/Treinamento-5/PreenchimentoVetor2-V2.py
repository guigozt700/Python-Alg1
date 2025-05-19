def exibe(L, n):
    for posicao, item in enumerate(L[ : n]):#Percorre os primeiros 'n' elementos de L (0 até n)
        #posição(indice) e o item(valor)
        print(f'N[{posicao}] = {item}')

def preenche(L, n, t):
    for i in range(n):   #Percorre até n(tamanho)
        L[i] = i % t          #Ex: 0%3=0 -> 1%3=1 -> 2%3=2 -> 3%3=0 -> 4%3=1 (reinicia os ciclos até o fim da lista)
 
def main():
    t = int(input())        #Define o tamanho do ciclo
    tamanho = 1000     #Define o tamanho da lista
    L = tamanho * [0]    #Cria a lista com mil posições com 0
    
    preenche(L, tamanho, t)  #Função para preencher a lista
    exibe(L, tamanho)

main()
