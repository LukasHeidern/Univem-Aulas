'''Implemente  um  programa  que  leia duas  strings,  str1  e  str2,  e  um  valor  
inteiro  positivo  N. Concatene não mais que N caracteres da string str2 a string str1.'''

str1 = input("Digite a primeira string: ")
str2 = input("Digite a segunda string: ")
while True:
    v = int(input("Quantos caracteres da primeira string deseja adicionar: "))
    if v not in range(len(str2)+1): print("valor excedeu o tamanho da string")
    else: break
print(str1 + str2[:v])
