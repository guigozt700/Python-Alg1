def preencher(lista):
    for i in range(10): #Percorre os indices da lista
        x = int(input())
        lista[i] = x #Adiona os valores em cada posição

def transforma(lista):
    i = 0
    while i < 10: #Percorre a lista novamente e altera os valores
        if lista[i] <= 0:
            lista[i] = 1
        i += 1

def exibe(lista):
    for i in range(len(lista)):
        print(f'X[{i}] = {lista[i]}') #Imprime o indice e o valor

def main():
    lista = 10 * [0] #Cria uma lista com 10 posições iniciadas com 0
    preencher(lista)
    transforma(lista)
    exibe(lista)

main()
