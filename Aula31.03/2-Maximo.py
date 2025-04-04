def maximo(a,b):
    if a>b:
        return a
    else:
        return b
x = int(input("Numero 1: "))
y = int(input("Numero 2: "))

m = maximo(x,y)

print("Maximo: %d" % m)
