

preco = 0
quant = 0
s_preco = 0

while True:
    preco = float(input("Digite o valor do produto: "))
    if preco == 0:
        break

    quant = int(input("Digite a quantas unidades: "))
    print()

    s_preco += preco * quant

if s_preco == 0:
    print("Nao comprou nada!")

else:
    print(f"O valor total da compra eh {s_preco} ")