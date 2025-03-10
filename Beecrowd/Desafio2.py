nomeVendedor = input()
salarioFixo = float(input())
vendas = float(input())

comissao = 0.15 * vendas
total = salarioFixo + comissao

print(f'TOTAL = R$ {total:.2f}')
