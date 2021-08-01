'''
4) Elabore um algoritmo que leia um numero inteiro e determine
quantos algoritmos ele possui. Exemplos:

Num == 23456 -> 5 algarismos
Num == 9876789 -> 7 algarismos
'''

num = int(input("Digite o numero inteiro: "))
i = 1
while num > 9:
    num = num // 10
    i += 1
print(f"{i} algarismos")
