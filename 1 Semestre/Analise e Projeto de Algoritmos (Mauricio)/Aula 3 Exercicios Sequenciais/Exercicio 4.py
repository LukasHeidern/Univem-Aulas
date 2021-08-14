'''4) Faça um algoritmo que leia dois valores inteiros e positivos e armazene 
nas variáveis A e B respectivamente. Em seguida troque o conteúdo das variáveis, 
ou seja, A deverá receber o valor de B e B o valor de A. '''

A = int(input("Digite o primeiro algarismo: "))
B = int(input("Digite o Segundo algarismo: "))

print("Os valores iniciais sao: A - {A}, B - {B}")

aux = A
A = B
B = aux

print("OS valores trocados sao: : A - {A}, B - {B}")


'''
Solucao exclusiva para Python

A,B = B,A

'''