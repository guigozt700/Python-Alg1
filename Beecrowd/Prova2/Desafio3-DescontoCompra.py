def main():
    compra = float(input())
    qtd = int(input())

    valorAntes = compra * qtd #5000

    descont = 10/100 #10%
    desc = 1/100 #1% -> a cada unidade
    desc = desc * qtd #% a cada produto

    somaDesconto = descont + desc #15%

    valorDepois = valorAntes * somaDesconto
    totalCompra = valorAntes-valorDepois

    print(f'{valorAntes:.2f}')
    print(f'{totalCompra:.2f}')

main()
