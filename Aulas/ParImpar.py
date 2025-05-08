def numPar(num):
    if num % 2 == 0:
        return num + 2
    else:
        return num + 1
    
def numImpar(num):
    if num % 2 == 1:
        return num - 2
    else:
        return num - 1

num = int(input())

print(f'{numImpar(num)} {numPar(num)}')
