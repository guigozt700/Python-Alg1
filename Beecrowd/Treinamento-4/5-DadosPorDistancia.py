def main():
    jogadas = int(input())
    contJogadas = 0
    
    for _ in range(jogadas):
        pontosMaria = 0
        pontosJoao = 0

        #Arremos de Joao
        for _ in range(3):
            pontos, distancia = input().split()
            pontos = int(pontos)
            distancia = int(distancia)
            
            pontosJoao += pontos * distancia

        #Arremessos de Maria
        for _ in range(3):
            pontos, distancia = input().split()
            pontos = int(pontos)
            distancia = int(distancia)
            
            pontosMaria += pontos * distancia


        #Após 3 arremessos de cada, ele compara, depois mais 3 arremssos de cada (6 arremessos para cada)    
        if pontosJoao > pontosMaria:
            print('JOAO')
        elif pontosJoao < pontosMaria:
            print('MARIA')
        else:
            print('EMPATE')

main()
