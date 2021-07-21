'''3.) No Brasil, temos regras para quem pode ou não votar. Vejam:
Idade < 16  “Votar é proibido!”
Idade >=16 e idade < 18 ou  idade >= 65  “Votar é facultativo!”
Idade >=18 e idade < 65  “Votar é obrigatório!”
Elabore um algoritmo que leia da idade de uma pessoa e determina sua situação 
com relação  ao seu voto.
'''

idade = int(input("Digite a idade do eleitor: "))

if idade > 0 and idade < 16: print("Votar é proibido!")
elif idade < 18: print("Votar é facultativo!")
elif idade < 65: print("Votar é obrigatório!")
else: print("Idade Invalida!")