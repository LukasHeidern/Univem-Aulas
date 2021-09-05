def base_check(base):
    if base not in [2, 4, 8, 10, 16]: return False
    return True

def value_check(base, value):
    for algarism in map(int, list(str(value))):
        if algarism not in range(base):return False
    return True

def base2dec(base, value):
    v = []
    c_value = 0
    for algarism in list(str(value)):
        v.insert(0,"ABCDEF".index(algarism) + 10 if algarism in "ABCDEF" else int(algarism))

    for position, algarism in enumerate(v):
        c_value += algarism * base ** position
    return c_value

def dec2base(base, value):
    c_value = []
    result = value

    while result != 0:
        rest = result % base
        c_value.insert(0, "ABCDEF"[rest - 10] if 10 >= rest <= 15 and base == 16 else str(rest))
        result = result // base

    if base != 16: return int("".join(c_value))
    else: return "".join(c_value)

def main():
    while True:
        print(f"1 - Converter base 10 para base 'n';\n"
              f"2 - Converter base 'n' para base 10;\n"
              f"0 - sair.")
        op = input("Digite a opcao que deseja:")

        if op in '12':
             while True:
                 base = int(input("Digite a base"))
                 if base_check(base): break
                 else: print("Base Invalida!")
             if op == '2':
                 while True:
                     value = int(input("Digite o valor: "))
                     if value_check(base,value): break
                     else: print("Valor Invalido!")
                 print(f"valor na base {base}: {value}\n"
                       f"valor na base 10: {base2dec(base,value)}")

             if op == '1':
                 value = int(input("Digite o valor: "))
                 print(f"valor na base 10: {value}\n"
                       f"valor na base {value}: {dec2base(base,value)}")
        if op == 0: break
        else: print("Opcao Invalida!")


main()