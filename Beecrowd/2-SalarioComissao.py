def total(salarioFixo,vendas):
    comissao = 0.15 * vendas
    total = salarioFixo + comissao
    return total

nomeVendedor = input()
salarioFixo = float(input())
vendas = float(input())

print(f'TOTAL = R$ {total(salarioFixo,vendas):.2f}')