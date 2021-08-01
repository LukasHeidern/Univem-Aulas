'''6.) Elabore um algoritmo que leia 3 medidas (a, b e c). 
Verifique se elas podem ser medidas de um triângulo. Caso sejam, 
determine se este triângulo é equilátero, isósceles ou escaleno.
'''

a = int(input("Digite o valor do primeiro lado: "))
b = int(input("Digite o valor do segundo lado: "))
c = int(input("Digite o valor do terceiro lado: "))

if a > b: a,b = b,a
if a > c: a,c = c,a
if b > c: b,c = c,b

'''
ou tambem

if a > b or a > c:
    if b < c: b,a = a,b
    else: c,a = a,c
if b > c: b,c = c,b
'''

if a > b+c and b > c+a and c > a+b:
    if a == b == c: print("Triangulo Equilatero")
    elif a == b != c or b == c != a or c == a != b: print("Triangulo Isoceles")
    else: print("Triangulo Escaleno")
else: print("Essas medidas nao formam um triangulo!")
