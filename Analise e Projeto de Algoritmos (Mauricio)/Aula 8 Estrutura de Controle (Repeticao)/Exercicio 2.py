n = int(input("Digite o numero a ser fatorado: "))

print(f"{n}! =",end=" ")

if n < 0:
    print("Nao existe fatorial de numeros negativos!")

else:
    result = 1
    for i in range(n, 0, -1):
        print(f"{i} *",end=" ")
        result *= i
    print(f"\b\b= {result}")