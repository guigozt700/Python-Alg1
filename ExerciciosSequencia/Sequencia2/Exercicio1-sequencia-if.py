numero = int(input('Numero inteiro com 4 digitos: '))

numE = numero // 100
numD = numero % 100
somaDigitos = numE + numD

somaDigitos *= somaDigitos

if somaDigitos == numero :
    print(f'O Número {numero} é igual ao Número {somaDigitos}')
else:
    print(f'Os números não são iguais')
