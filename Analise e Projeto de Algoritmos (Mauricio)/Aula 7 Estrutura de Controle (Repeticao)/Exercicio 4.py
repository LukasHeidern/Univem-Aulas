while True:
    op = input("Digite o Operador: ")
    result = 0

    if (op != '+') and (op != '-') and (op != '*') and (op != '/') and (op != '#'):
        print("Operador invalido!")

    else:
        if op == '#':
            print("Encerrando!")
            break

        n1 = float(input("Digite o valor 1: "))
        n2 = float(input("Digite o valor 2: "))

        if op == '+':
            result = n1 + n2

        elif op == '-':
            result = n1 - n2

        elif op == '*':
            result = n1 * n2

        elif op == '/':
            if n2 == 0:
                print("Operacao invalida (Divisao por 0)")

            else:
                result = n1 / n2

        print(f"O resultado eh {result}")