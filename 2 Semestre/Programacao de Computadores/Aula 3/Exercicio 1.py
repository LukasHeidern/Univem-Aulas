'''1.Faça um programa em Python que leia uma palavra pelo teclado e faça a impressão 
conforme o exemplo a seguir para a palavra AMOR:
A
AM
AMO
AMOR'''

string = input("Digite uma palavra: ")
for i in range(len(string)+1): print(string[0:i])
