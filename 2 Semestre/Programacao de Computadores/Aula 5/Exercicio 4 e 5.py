### Exercicio 4 e 5
def primo(v):
    for i in range(2,(v//2)+1):
        if v % i == 0: return False
    return True

### Exercicio 4

valor = int(input("Digite um valor: "))
if primo(valor): print(f"{valor} e primo!")
else: print(f"{valor} nao e primo!")
print("\n\n")

### Exercicio 5

f = int(input("Digite o valor do final da contagem: "))
primos = []
for i in range(2,f+1):
    if primo(i): primos.append(i)
print("Os valores primos sao: ",*primos)

