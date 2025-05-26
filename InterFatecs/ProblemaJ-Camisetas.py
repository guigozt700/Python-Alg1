#Versão memoizada

def lucroMaximo(qtdTecido, teCamisa1, lucro1, teCamisa2, lucro2, teCamisa3, lucro3, memo={}):
    # Programação dinamica -> memo vai guardar uma "anotação" ou "lembrente"
    
    if qtdTecido < min(teCamisa1, teCamisa2, teCamisa3):
        return 0

    if (qtdTecido, teCamisa1, lucro1, teCamisa2, lucro2, teCamisa3) not in memo:  
        #Se tem tecido suficiente para fazer o teCamisa1, faz...
        if qtdTecido >= teCamisa1:
            # Função recursiva              (retorna a sobra de tecido), mesmos parametros atualizados
            cenario1 = lucro1 + lucroMaximo(qtdTecido - teCamisa1, teCamisa1, lucro1, teCamisa2, lucro2, teCamisa3, lucro3 )
        else:
            cenario1 = 0

        #Se tem tecido suficiente para fazer o teCamisa2, faz...
        if qtdTecido >= teCamisa2:
            cenario2 = lucro2 + lucroMaximo(qtdTecido - teCamisa2, teCamisa1, lucro1, teCamisa2, lucro2, teCamisa3, lucro3 )
        else:
            cenario2 = 0

        #Se tem tecido suficiente para fazer o teCamisa3, faz...
        if qtdTecido >= teCamisa3:
            cenario3 = lucro3 + lucroMaximo(qtdTecido - teCamisa3, teCamisa1, lucro1, teCamisa2, lucro2, teCamisa3, lucro3 )
        else:
            cenario3 = 0

        #Chave do dicionario
        memo[(qtdTecido, teCamisa1, lucro1, teCamisa2, lucro2, teCamisa3)] = max(cenario1, cenario2, cenario3)

    return memo[(qtdTecido, teCamisa1, lucro1, teCamisa2, lucro2, teCamisa3)]

def main():
    qtd_tecido = int(input())
    tecidoCamiseta1, lucro1 = map(int, input().split()) #map([int('a'), int('b')]) -> [a,b] gera uma "lista"
    tecidoCamiseta2, lucro2 = map(int, input().split())
    tecidoCamiseta3, lucro3 = map(int, input().split())
    
    print(lucroMaximo(qtd_tecido,
                      tecidoCamiseta1, lucro1,
                      tecidoCamiseta2, lucro2,
                      tecidoCamiseta3, lucro3))

main()
