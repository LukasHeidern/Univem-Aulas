'''1) Escreva um algoritmo que leia a altura e o sexo de uma pessoa. Calcule 
e imprima o seu peso ideal utilizando as seguintes fórmulas:	
    Para homens: (72.7*h)-58;
    Para mulheres: (62.1*h)-44.7
'''

sexo = input("Digite o sexo da pessoa: ")[0]
alt = float("Digite a altura da pessoa: ")

if sexo in 'Mm': peso_ideal = (72.7 * alt) - 58
elif sexo in 'Ff': peso_ideal = (62.1 * alt) - 44.7

print(f"O peso ideal e {peso_ideal}")