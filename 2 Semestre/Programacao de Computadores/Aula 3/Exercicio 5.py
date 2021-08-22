'''5.Elabore um programa em Python que lê uma String e calcule e imprima um código 
utilizando a seguinte regra: para cada vogal, somar 5 pontos, para cada consoante somar 
10 pontos, desconsiderando qualquer outro caractere.'''

import unidecode
string = input("Digite uma string: ").lower()
string = unidecode.unidecode(string)
codigo = 0
for i in string:
    if ord(i) in range(65,91) or  ord(i) in range(97,122):
        if i in 'AEIOUaeiou': codigo += 5
        else: codigo += 10
print(f"O codigo e: {codigo}")
