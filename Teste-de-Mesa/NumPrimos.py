def primo(n):
    qtd = 0
    pd = 1

    while pd <= n:
        if n % pd == 0:
            qtd += 1
        pd += 1
        
    if qtd == 2:
        return True
    else:
        return False

n = int(input())

if primo(n):
    print('é primo')
else:
    print('não é primo')
