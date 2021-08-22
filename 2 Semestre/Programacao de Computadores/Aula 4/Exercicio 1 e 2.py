'''1.Faça um programa em Python que leia uma palavra pelo teclado e faça a impressão 
conforme o exemplo a seguir para a palavra AMOR:
A
AM
AMO
AMOR'''

'''2.Faça um programa em Python que leia uma palavra pelo teclado e faça a impressão 
conforme o exemplo a seguir para a palavra AMOR

AMOR
AMO
AM
A'''

#######################################################################################

def ex01():
    string = input("Digite uma palavra: ")
    for i in range(len(string)+1): print(string[0:i])

def ex02():
    string = input("Digite uma palavra: ")
    for i in range(0,len(string)+1,-1): print(string[0:i])

def main():
    op = int(input(f"1 > exercicio 1"
                    "\n2 > exercicio 2"
                    "\nOpcao>> "))
    if op == 1:
        ex01()
    elif op == 2:
        ex02()

main()
