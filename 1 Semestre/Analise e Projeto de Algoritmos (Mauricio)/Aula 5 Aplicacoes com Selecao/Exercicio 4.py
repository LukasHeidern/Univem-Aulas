'''4) Uma loja, lançou uma grande promoção a seus clientes... 
Dependendo do valor da compra, um certo desconto será concedido, 
como mostrado abaixo:

20% se o valor da compra for maior ou igual a R$ 500,00
15% se for maior ou igual a R$200,00 e menor que R$ 500,00 
10% caso seja menor que R$200,00. 

Escreva um algoritmo que após ler o valor da compra, calcule e mostre: 
o valor da compra do cliente
o valor do desconto obtido 
o valor a ser pago pelo cliente.
'''

v_total = float("Digite o valor total da compra do cliente: ")

if v_total > 0 and v_total < 200: v_final = v_total * 0.10
elif v_total < 500: v_final = v_total * 0.15
elif v_total > 500: v_final = v_total * 0.20

print(f"O valor sem desconto e {v_total} e o valor a ser pago e {v_final}")