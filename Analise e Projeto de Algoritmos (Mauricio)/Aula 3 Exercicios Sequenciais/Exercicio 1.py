'''1) Um funcionário recebe um salário fixo mais 4% de comissão 
sobre as vendas. Faça um programa que receba o salário fixo de um 
funcionário e o valor de suas vendas, calcule e mostre a comissão e 
o salário final do funcionário.'''

salario = float(input("Digite o valor do seu salario: "))
vendas = float(input("Digite o valor total de suas vendas: "))

salario_final = salario + (vendas * 0.04)

print(f"Seu salario final e R${salario_final}")