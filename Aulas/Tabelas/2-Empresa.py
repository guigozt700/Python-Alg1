#Matheus Oliveira;1000.0;3;sim
#Aline dos Santos;4000.0;4;sim
#Carla Oliveira;2500.0;2;não
#Leon Kennedy;10000.0;10;sim    

funcionarios = []

entrada = input()

while entrada != '':
    funcionario = entrada.split(';')          #divide a entrada com ";"
    funcionario[1] = float(funcionario[1])
    funcionario[2] = int(funcionario[2])
    funcionario[3] = (funcionario[3] == 'sim')
    funcionarios.append(funcionario)

    entrada = input()
print('-' * 47)
print(f'{"NOME":^16} | {"SALÁRIO":^11} | {"TEMPO":^7} | META')
print('-' * 47)

for funcionario in funcionarios:
    nome, salario, tempo, meta = funcionario #desempacota os indices dos funcionarios nas variaveis
    print(f'{nome:16}', end=' | ')
    print(f'R$ {salario:8.2f}', end=' | ')
    print(f'{tempo:02} anos', end=' | ')
    print(f'{("😃" if meta else "🥲"):^4}')
print('-' * 47)

bonus = []

for nome, salario, tempo, meta in funcionarios:
    valor = salario + 0.05 * tempo * salario
    if meta:
        valor += 0.10 * valor
    bonus.append([nome, valor])

for registro in bonus:
    nome, valor = registro
    print(f'{nome} | R${valor:.2f}')
