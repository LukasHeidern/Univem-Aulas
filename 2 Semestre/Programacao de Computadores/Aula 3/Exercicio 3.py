'''3.Escreva  um  programa  em Python que  leia  uma frase e  informe  a  quantidade  
de  palavras presentes na string.'''

string = input("Digite uma frase: ")
print(f"Existem {len(string.split())} palavras na frase: \n{string}")
