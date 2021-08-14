'''
1) Elabore um algoritmo que leia um numero e
calcule a soma dos numeros menores ou iguais
a ele, comecando pelo 1.

Ex.: para num == 10, o algoritmo devera
calcular:
1+2+3+4+5+6+7+8+9+10 = 55
'''

num = int(input("Digite o numero: "))

i = 1
resultado = 0

while i <= num:
    resultado += i
    i += 1

print(f"Resultado = {resultado}")
