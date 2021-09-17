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

    quit = False

    while not quit:
        while True:
            i_base = input("Digite a a base de entrada: ")
            if base_check(i_base):
                i_base = int(i_base)
                break
            else: print("Opcao invalida!")

        while True:
            o_base = input("Digite a a base de saida: ")
            if base_check(o_base):
                o_base = int(o_base)
                break
            else: print("Opcao invalida!")

        while True:
            value = input("Digite o valor: ").upper()
            if value_check(i_base,value): break
            else: print("Valor Invalido!")

        n_value = dec2base(o_base,base2dec(i_base,value))

        print(f"\nValores"
              f"\nBase {i_base}: {value}"
              f"\nBase {o_base}: {n_value}\n")

        if input("Deseja Sair?: ")[0] in "YySs": quit = True


##-------------------------##
main()
