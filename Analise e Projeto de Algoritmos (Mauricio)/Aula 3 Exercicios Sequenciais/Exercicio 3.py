'''3) Elabore um algoritmo que leia um numero inteiro (max. 3 algarismos) 
e mostre os algarismos em separado. Ex. NUM == 725 o algoritmo produzirá: 
Centena = 7, Dezena = 2 e Unidade = 5.'''

num = int(input("Digite um numero: "))
u = num % 10
d = num % 100  // 10
c = num // 100
print(f"Unidade {u}, Dezena {d}, Centena {c}")