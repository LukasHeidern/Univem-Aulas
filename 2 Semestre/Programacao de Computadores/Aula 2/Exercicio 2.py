'''2.Escreva um programa que substitui as ocorrências de um caractere ‘0’ em uma string por 
outro caractere ‘1’.Imprima o antes e o depois.'''

string = input("Digite uma string contendo somente 0's e 1's: ")
print(string)
string = string.replace('0','1')
print(string)