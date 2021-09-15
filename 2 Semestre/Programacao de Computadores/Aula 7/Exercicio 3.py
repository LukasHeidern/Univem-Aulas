
def mdc(a,b):
    if b <= a and a % b == 0: return b
    elif a < b: return mdc(b,a)
    return mdc(b, a % b)

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
print(f"MDC = {mdc(a,b)}")