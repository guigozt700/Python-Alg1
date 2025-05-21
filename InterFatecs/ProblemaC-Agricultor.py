def main():

    qtdLeituras = int(input())
    
    for i in range(qtdLeituras):
        temperatura, umidade, previsao = input().split()
        temperatura = float(temperatura)
        umidade = float(umidade)
        previsao = float(previsao)
        
        if previsao == 1:
            print('NAO REGAR')
        elif temperatura > 30.0 and umidade <= 50.0:
            print('REGAR')
        else:
            print('NAO REGAR')

main()
