'''2.Faça um programa em Python que leia uma palavra pelo teclado e faça a impressão 
conforme o exemplo a seguir para a palavra AMOR

AMOR
AMO
AM
A'''

string = input("Digite uma palavra: ")
for i in range(0,len(string)+1,-1): print(string[0:i])

