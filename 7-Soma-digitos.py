numero = int(input('Digite um número: '))
digitosDireita = int(str(numero)[2:])
digitosEsquerda = int(str(numero)[:2])

somaDigitos = digitosEsquerda + digitosDireita 

print('Numero digitado: ',numero)
print('Soma dos digitos (Esquerda:',digitosEsquerda,') + (Direita: ',digitosDireita,') = ',somaDigitos)
