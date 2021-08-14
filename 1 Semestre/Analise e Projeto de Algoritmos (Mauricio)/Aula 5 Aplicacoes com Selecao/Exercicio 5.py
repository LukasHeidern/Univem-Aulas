'''O IMC – Índice de Massa Corporal é calculado pela seguinte fórmula:
IMC = peso/altura**2
Elabore um algoritmo que calcule leia o peso e a altura de uma pessoa e 
calcule o seu  IMC. Em seguida  mostre a sua classificação:

< 18,5          Peso Baixo
  18,5 - 24,9   Peso Normal
  25,5 - 29.9   Sobrepeso
  30,0 - 34,9   Obesidade (I Grau)
  35,0 - 39,9   Obesidade Severa (II Grau)
>= 40,0         Obesidade Morbida (III Grau)
'''
peso = float(input("Digite o Peso:"))
altura = float(input("Digite a Altura:"))

imc = peso / altura ** 2

if imc < 18.5: print("Peso Baixo")
elif imc < 25.5:print("Peso Normal")
elif imc < 30.0:print("Sobrepeso")
elif imc < 35.0:print("Obesidade (I Grau)")
elif imc < 40.0:print("Obesidade Severa (II Grau)")
else: print("Obesidade Morbida (III Grau)")