'''4.Faça  um  programa em  Python que leia uma  lista  de nomes e  depois  coloque-os  
em  ordem alfabética. Pode  pedir  a  lista  de  nomes  usando  split()  ou  pedindo  a  
quantidade  de  nomes  antes  do laço, ou ainda, dentro do laço, perguntar a cada 
entrada se deseja entrar com mais um nome.'''

nomes = []
n = ""
while True:
    n = input("Digite um nome ou digite 'q' para sair: ")
    if n == 'q':_break
    else: nomes.append(n)
nomes = nomes.sort()
for i in nomes:
    print(*i)

