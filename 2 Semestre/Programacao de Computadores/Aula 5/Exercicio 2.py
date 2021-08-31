def potencia(b,e):
    return b**e

base = int(input("Digite o valor da base:"))
expoente = 0

while True:
    expoente = int(input("Digite o valor do expoente: "))
    if expoente < 0: print("Expoente invalido")
    else: break
print(f"O valor da potencia e {potencia(base,expoente)}")



