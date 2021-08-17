'''7.Faça um programa que contenha um menu com as seguintes opções: 
    (a) Ler uma string S1
    (b) Imprimir o tamanho da string S1; 
    (c) Comparar a string S1 com uma nova string S2 fornecida pelo usuário e imprimir o 
resultado da comparação;
    (d)  Concatenar  a  string  S1  com  uma  nova  string  S2  e  imprimir  na  tela  
o  resultado  da concatenação;(e) Imprimir a string S1 de forma reversa; 
    (f)Contar quantas  vezes  um  dado  caractere  aparece  na  string  S1.  Esse  
caractere  desse  ser informado pelo usuário; 
    (g)Substituir a primeira ocorrência do caractere C1 da string S1 pelo caractere C2. 
Os caracteres C1 e C2 serão lidos pelo usuário; 
    (h) Verificar se uma string S2 é substring de S1. A string S2 deve ser informada 
pelo usuário;
    (i) Criar uma  substring  da  string  S1.  Para  isso  o  usuário  deve  informar  a  
partir  de qual  posição deve ser criada a substring e qual é o tamanho da substring.
Imprima a substring.
    (j) Imprimir quantos caracteres estão em maiúsculo.'''


##############################################################################

op = input(f"Digite uma opcao:"
    "\n(a) Ler uma string S1;"
    "\n(b) Imprimir o tamanho da string S1;" 
    "\n(c) Comparar a string S1 com uma nova string S2;"
    "\n(d)  Concatenar  a  string  S1  com  uma  nova  string  S2;"
    "\n(e) Imprimir a string S1 de forma reversa;"
    "\n(f)Contar quantas  vezes  um  dado  caractere  aparece  na  string  S1;"
    "\n(g)Substituir a primeira ocorrência do caractere C1 da string S1 pelo caractere C2."
"Os caracteres C1 e C2 serão lidos pelo usuário;"
    "\n(h) Verificar se uma string S2 é substring de S1;"
    "\n(i) Criar uma  substring  da  string  S1;"
    "\n(j) Imprimir quantos caracteres estão em maiúsculo."
    "\n>>> ")
s1 = ""

# (a) Ler uma string S1 
if op == 'a': 
    s1 = input("Digite uma string: ")
    print(f"String: {s1}")

# (b) Imprimir o tamanho da string S1
if op == 'b': print(f"Tamanho da string 1: {len(s1)}")

# (c) Comparar a string S1 com uma nova string S2
if op == 'c': 
    s2 = input("Digite outra string: ")
    if s1 == s2: print("Strings Iguais")
    else: print("Strings Diferentes")
 
# (d)  Concatenar  a  string  S1  com  uma  nova  string  S2
if op == 'd': 
    s2 = input("Digite outra string: ")
    print(f"Nova String: {s1+s2}")

# (e) Imprimir a string S1 de forma reversa
if op == 'e': print(s1[::-1])

# (f)Contar quantas  vezes  um  dado  caractere  aparece  na  string  S1
if op == 'f':
    c = input("Digite o caractere que deseja contar: ")
    print(f"Existem {s1.count(c)} caracteres {c}" )

# (g)Substituir a primeira ocorrência do caractere C1 da string S1 pelo caractere C2.
if op == 'g':
    c1 = input("Digite o caractere a ser substituido: ")
    c2 = input("Digite o caractere a substituir: ")
    s1 = s1.replace(c1,c2)
    print(s1)

# (h) Verificar se uma string S2 é substring de S1
if op == 'h':
    s2 = input("Digite outra string: ")
    if s2 in s1: print("E substring")
    else: print("Nao e substring")

# (i) Criar uma  substring  da  string  S1
if op == 'i':
    p = input("Digite os valores de inicio e de fim da substring (Separados por espaco): ").split()[0:1]
    s2 = s1[p[0]:p[1]]
    print(s2)

# (j) Imprimir quantos caracteres estão em maiúsculo
if op == 'j':
    n = 0
    for i in s1:
        if i.isupper(): n += 1
    print(f"Existem {n} caracteres Maiusculos")
    
