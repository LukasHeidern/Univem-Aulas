
num = int(input("Digite o numero:"))
print(f"Divisores de {num} -",end=" ")

for i in range(1, (num//2) + 1):
    if num % i == 0:
        print(f"{i}",end=" ")