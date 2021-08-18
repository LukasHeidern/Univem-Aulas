'''3.Escreva  um  programa  em Python que  leia  uma frase e  informe  a  quantidade  
de  palavras presentes na string.'''

'''4.Faça  um  programa em  Python que leia uma  lista  de nomes e  depois  coloque-os  
em  ordem alfabética. Pode  pedir  a  lista  de  nomes  usando  split()  ou  pedindo  a  
quantidade  de  nomes  antes  do laço, ou ainda, dentro do laço, perguntar a cada 
entrada se deseja entrar com mais um nome.'''

def ex03():
    string = input("Digite uma frase: ")
    print(f"Existem {len(string.split())} palavras na frase: \n{string}")


def ex04():
    nomes = []
    n = ""
    while True:
        n = input("Digite um nome ou digite 'q' para sair: ")
        if n == 'q': break
        else: nomes.append(n)
    nomes = nomes.sort()
    for i in nomes:
        print(*i)

def main():
    op = int(input(f"1 > exercicio 3"
                    "\n2 > exercicio 4"
                    "\nOpcao>> "))
    if op == 1:
        ex03()
    elif op == 2:
        ex04()

main()