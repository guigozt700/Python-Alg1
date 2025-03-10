numero = int(input('Digite um número maior que 10: '))
doisDigitos = (numero // 100) * 100
calc = numero - doisDigitos

print('Os dois ultimos digitos de',numero,'são:',calc)
