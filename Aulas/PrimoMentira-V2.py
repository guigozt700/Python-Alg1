from time import time

def tempo(f, *a): #parametros: função(geraLista) e a variavel (limite)
    inicio = time() # salva o tempo antes de executar
    r = f(*a) #executa a função

    return  (r, time() - inicio) #retorna o resultado(r) e o tempo que levou para executar

def geraLista(limite):
    L = []

    for n  in range(1, limite+1):
        if mentirinha(n):
            L.append(n)

    return L

def mentirinha(n): #Verifica se o numero tem exatamente 3 divisores
    qtdDivisores = 0
    metade = n // 2

    for pd in range(2, metade+1): # Percorre até a metade no numero (ex: 6 -> div: 2, 3, 6)
        if n % pd == 0: 
            qtdDivisores += 1
            
            if qtdDivisores == 2:
                return False 

    return qtdDivisores ==1 

def main():

    limite = int(input('Limite: '))

    L, t = tempo(geraLista, limite)
    print(f'Tempo: {t:.2f} seg')
    print(f'Lista [{L}]')

main()
