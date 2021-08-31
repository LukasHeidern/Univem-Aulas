def inverte(valor):
    if str(valor)[0] == '-': return int('-' + str(valor)[:0:-1])
    else: return int(str(valor)[::-1])

n = int(input("Digite um valor para inversao: "))
print(f"O valor invertido e {inverte(n)}")