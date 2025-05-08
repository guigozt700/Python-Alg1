def primo(n):
    qtd = 0
    for pd in range(1,n+1): #range percorre de 1 até n +1 (para inclui-lo)
        if n % pd == 0:     #n será dividido por pd, qtd recebera os valores que darão 0   
            qtd += 1
    if qtd == 2:            #se qtd for igual a 2 (primos só são divididos por 1 e por ele mesmo)
        return True
    else:
        return False

def main():
    casos = int(input())

    for i in range(casos):  
        n = int(input())

        if primo(n):
            print('Prime')
        else:
            print('Not Prime')


main()
