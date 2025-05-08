def cabecalho():
    print('FATEC DIADEMA')

contLinha = 5

for i in range(16):
    if contLinha > 4:
        cabecalho()
        contLinha = 1

    print('testando a funcao cabecalho')
    contLinha += 1
