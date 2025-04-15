def par(num):
    return num % 2 == 0

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

qtdPares = 0

if par(a):
    qtdPares += 1
    
if par(b):
    qtdPares += 1
    
if par(c):
    qtdPares += 1
    
if par(d):
    qtdPares += 1
    
if par(e):
    qtdPares += 1
    
print(f'{qtdPares} valores pares')
