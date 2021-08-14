'''
5) Elabore um algoritmo que leia um numero inteiro
e o inverta. Veja alguns exemplos:

Num = 1234 -> Invertido = 4321
Num = 564378 -> Invertido = 873465
'''



num = int(input("Digite o valor do numero: "))
div = num
alg = 0
i = 0
inv = 0

while div > 0:
    div //= 10
    i += 1

while num > 0:
    alg = num % 10
    num //= 10
    inv += alg * (10 ** i)
    i -= 1

print(inv//10)