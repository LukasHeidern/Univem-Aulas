'''1) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar 
o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior 
que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve 
pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um 
algoritmo que leia a variável P (peso de peixes) e verifique se há excesso. 
Se houver, calcular quanto foi o excesso e qual será o valor da multa que João deverá 
pagar. '''

p = int(input("Quantos quilos (Kg)?: "))
if p > 50:
    v = p - 50 * 4.00
    print(f"Acima da quantidade permitida por {p -50} Kg's  voce tera que pagar {v} R$")
else: print("Nao ha peso excedente!") 