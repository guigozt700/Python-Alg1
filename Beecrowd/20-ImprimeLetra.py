qtd = int(input('Quantidade: '))
cont = 0
vogais = 0

while cont < qtd:
    letra = input('Letra: ')
    if letra == 'a' or letra == 'e' or letra == 'i' or letra =='o' or letra == 'u':
        vogais += 1
    cont += 1
print(f'Vogais: {vogais}')
