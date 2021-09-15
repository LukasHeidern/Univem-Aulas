

def powered(n,e):
    if e == 0: return n
    return n * powered(n,e-1)

n = int(input("Digite o valor da base: "))
e = int(input("Digite o valor do expoente: "))
print(powered(n,e))