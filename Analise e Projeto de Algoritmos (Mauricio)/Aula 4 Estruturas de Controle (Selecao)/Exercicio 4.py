'''4) Idem ao 2) porém com três valores. '''

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a > b and a > c: print("O primeiro valor e o maior!")
elif b > c: print("O segundo valor e o maior!")
else: print("O terceiro valor e o maior!")