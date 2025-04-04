def areaTriangulo(a,c):
    return (a*c) / 2
    
def areaCirculo(c):
    return 3.14159 * c**2
    
def areaTrapezio(a,b,c):
    return (a+b) * c /2

def areaQuadrado(b):
    return b**2
    
def areaRetangulo(a,b):
    return a*b

a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

print(f'TRIANGULO: {areaTriangulo(a,c):.3f}')
print(f'CIRCULO: {areaCirculo(c):.3f}')
print(f'TRAPEZIO: {areaTrapezio(a,b,c):.3f}')
print(f'QUADRADO: {areaQuadrado(b):.3f}')
print(f'RETANGULO: {areaRetangulo(a,b):.3f}')
