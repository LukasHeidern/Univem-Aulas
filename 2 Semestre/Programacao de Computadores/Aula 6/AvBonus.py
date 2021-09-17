#### Lucas Ferrari Lopes - 617571


def get_values():
    values = []
    while True:
        v = input("Digite o valor que deseja adicionar ou digite 0 para sair: ")
        if v.isnumeric() and int(v) > 0: values.append(int(v))
        elif v == '0': break
        else: print("Valor invalido")
    return values

def r_primes(end, start=2):
    primes = []
    for v in range(start,end):
        yn = True
        for i in range(2,v):
            if v % i == 0: yn = False; break
        if yn: primes.append(v)
    return primes


def decomposition(values):
    matrix = [values]
    result = []
    primes = r_primes(max(values))
    i = 0
    p = []
    while any(x != 1 for x in matrix[-1]):
        while any(y % primes[i] == 0 for y in matrix[-1]):
            for v in matrix[-1]:
                if v % primes[i] == 0: result.append(v // primes[i])
                else: result.append(v)
            if primes[i] not in p: p.append(primes[i])
            matrix[-1].append(primes[i])
            matrix.append(result)
            result = []
        i += 1
    mmc = 1
    for i in matrix[0:-1]:
        mmc *= i[-1]
    
    return p,matrix,mmc


def main():
    values = get_values()
    if len(values) > 0:
        primes,matrix,mmc = decomposition(values)

        print("Decomposicao")
        for l,line in enumerate(matrix):
            for e,element in enumerate(line):
                if e == len(line)-1 and l != len(matrix)-1: print(f'    |{element:5}')
                else: print(f'{element:5}',end="")
        print(f"\n\nPrimos:{primes}")

        print(f"MMC: {mmc}")

main()
