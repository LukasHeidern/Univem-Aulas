
a = input("Digite o valor das notas separados por espaco: ").split()
for i in range(len(a)): a[i] = float(a[i])
for i in a: print(i,end=" ")
print("Valores lidos: ",len(a))
soma = sum(a)
print("Media: ", (soma / len(a)))
a.remove(min(a))
print("notas iguais a 10.0: ",a.count(10.0))
del a[0]
a.pop(-1)
print(a)



