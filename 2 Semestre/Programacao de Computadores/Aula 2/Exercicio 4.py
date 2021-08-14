'''4.Faça um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da 
palavra. Imprima a string resultante.'''

sermo = list(input("Digite uma palavra:"))
for i,p in enumerate(sermo):
    sermo[i] = chr((ord(p))+1)
sermo = "".join(sermo)
print(f"Nova string: {sermo}")