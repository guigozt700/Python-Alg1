def resultado(dorothy, dagmar):
    r = ('DOROTHY' if dorothy > dagmar else 'DAGMAR') + ' DECIDE'
    return r + (' E A NONNA VAI' if dorothy + dagmar > 40 else '')
 
def main():
    qtd_pares = int(input())
 
    for i in range(qtd_pares):
        dorothy = int(input())
        dagmar = int(input())
        print(resultado(dorothy, dagmar))
 
main()
