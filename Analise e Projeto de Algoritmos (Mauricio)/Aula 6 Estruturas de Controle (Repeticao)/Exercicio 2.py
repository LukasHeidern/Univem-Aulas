'''
2) Elabore um algoritmo para mostrar a tabuada
de um numero N qualquer lido pelo teclado.
Por exemplo, se N == 7, devera ser mostrado:
7*1, 7*2, 7*3, ..., 7*10.
'''

n = int(input("Digite o numero: "))
i = 1

while i <= 10:
    print(f"{n} * {i} = {n*i}")
    i += 1
