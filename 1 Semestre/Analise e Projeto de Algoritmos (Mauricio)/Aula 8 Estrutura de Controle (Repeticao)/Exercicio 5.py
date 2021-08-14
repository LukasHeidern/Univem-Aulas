
while True:
    num = int(input("Digite o numero: "))
    soma = 0

    if num > 0:
        for i in range(1, (num // 2) + 1):
            if num % i == 0:
                soma += i
                print(f"{i} +",end=" ")

        print(f"\b\b= {soma}")
        if soma == num:
            print(f"{num} eh perfeito!")

        else:
            print(f"{num} nao eh perfeito!")

    else:
        print(f"Numero invalido!")

    sn = input("Deseja tentar novamente? 'S' para Sim").upper()[0]
    if sn !='S':
        print(f"Encerrando")
        break