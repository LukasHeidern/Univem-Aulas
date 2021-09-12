#### Lucas Ferrari Lopes - 617571

## verifica a base
def base_check(base):
    if base not in ['2', '4', '8', '10', '16']: return False
    return True

## verifica os valores
def value_check(base, value):
    v = str(value)
    if base == 16:
        for algarism in v:
            if algarism not in "ABCDEF1234567890": return False

    elif v.isnumeric():
        for algarism in v:
            if int(algarism) not in range(base) : return False
    else: return False
    return True

## faz a conversao da base 'n' para decimal
def base2dec(base, value): # 2
    v = []
    c_value = 0
    for algarism in list(value):
        v.insert(0,"ABCDEF".index(algarism) + 10 if algarism in "ABCDEF" else int(algarism))

    for position, algarism in enumerate(v):
        c_value += algarism * base ** position
    return c_value

## faz a conversao de decimal para a base 'n'
def dec2base(base, value): # 1
    c_value = []
    result = value

    while result != 0:
        rest = result % base
        c_value.insert(0, "ABCDEF"[rest - 10] if rest in range(10,base) and base == 16 else str(rest))
        result = result // base

    if base != 16: return int("".join(c_value))
    else: return "".join(c_value)

## inicia o programa
def main():
    while True:
        while True:
            print(f"1 - Converter base 10 para base 'n';\n"
                  f"2 - Converter base 'n' para base 10;\n"
                  f"0 - sair.")
            op = input("Digite a opcao que deseja: ")
            if op in '120':break
            else: print("Opcao invalida!")

        if op == '2':
            while True:
                base = input("Digite a base: ")
                if base_check(base):
                    base = int(base)
                    break
                else: print("Base Invalida!")

            while True:
                value = input("Digite o valor: ").upper()
                if value_check(base,value): break
                else: print("Valor Invalido!")
            print(f"valor na base {base}: {value}\n"
                f"valor na base 10: {base2dec(base,value)}")

        elif op == '1':
            while True:
                base = input("Digite a base")
                if base_check(base):
                    base = int(base)
                    break
                else:print("Base Invalida!")

            while True:
                value = input("Digite o valor: ")
                if value.isnumeric():
                    value = int(value)
                    break
                else: print("Valor Invalido!")

            print(f"valor na base 10: {value}\n"
                f"valor na base {base}: {dec2base(base,value)}")

        elif op == '0': break

    print("Encerrado")

##-------------------------##
main()
