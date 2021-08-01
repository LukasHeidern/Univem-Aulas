
soma = 0
i = 0

while True:
    idade = int(input("Digite a idade: "))
    if idade == 0:
        break
    elif idade < 0:
        print("Idade invalida!")

    else:
        soma += idade
        i += 1

if soma == 0:
    print("Nao existe media!")

else:
    print(f"Media = {soma / i}")

