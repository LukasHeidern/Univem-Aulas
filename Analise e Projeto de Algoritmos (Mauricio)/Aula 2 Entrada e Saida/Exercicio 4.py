'''4) Faca um algoritmo que receba o preco de um produto, calcule e mostre o 
novo preco sabendo que este sofreu um desconto de 10%. '''

t_preco = float(input("Digite o preco do produto: "))
d_preco = t_preco - (t_preco / 100) * 10
print(f"O preco com desconto e {d_preco}")