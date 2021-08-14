'''8) Elabore um algoritmo que leia 3 valores inteiros (a,b e c) e os coloque em 
ordem crescente, de modo que em a fique o menor valor, em b o valor intermediário e 
em c o maior valor. '''


a = int(input("Digite o valor do primeiro valor: "))
b = int(input("Digite o valor do segundo valor: "))
c = int(input("Digite o valor do terceiro valor: "))

print(f"Antes: {a} - {b} - {c}")

if a > b: a,b = b,a
if a > c: a,c = c,a
if b > c: b,c = c,b

print(f"Depois: {a} - {b} - {c}")