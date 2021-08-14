
num =  int(input("Digite o valor do numero: "))
primo = True

for i in range(2, (num//2) + 1):
    if num % i == 0:
        primo = False
        break

if primo:
    print(f"{num} eh Primo!")

else:
    print(f"{num} nao eh Primo!")