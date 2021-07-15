'''2) Elabore um algoritmo que leia um valor em reais (R$) e mostre sua 
conversão para dólares ($). Para isto o algoritmo deverá solicitar ao 
usuário a cotação do dólar. Mostre o resultado. '''

real = float(input("Digite o valor em reais (R$) que deseja converter: "))
cotacao = float(input("Digite o valor da cotacao do dolar: "))

dolar = real / cotacao

print(f"O valor em dolares e: $ {dolar}")