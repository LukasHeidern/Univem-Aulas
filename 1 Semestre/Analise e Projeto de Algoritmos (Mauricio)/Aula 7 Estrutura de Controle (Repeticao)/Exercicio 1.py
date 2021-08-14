

while True:
    nota = float(input("Digite a nota: "))
    if nota < 0 or nota > 10:
        print("Nota invalida!")

    else:
        print(f"A nota eh {nota}")
        break