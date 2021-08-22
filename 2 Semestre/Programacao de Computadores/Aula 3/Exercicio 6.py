'''6.Faça  um  programa  em Python para  verificar  se um  CPF,  digitado  pelo  usuário,  
está  correto  ou não.  Para  isto  considere  uma  string  de  11  caracteres  para  
armazenar  sem  pontos  ou  traço,  apenas números (Faça a validação para a entrada ser 
apenas composta de números).A verificação do CPF está em calcular os dois dígitos de 
controle e comparar com os digitados, se os dois  calculados  forem  iguais  aos  dois  
digitados,  o  CPF  digitado  é  válido,  caso  contrário,  o  CPF  é inválido. Cálculo 
do 1º dígito: Soma os 9 primeiros números do CPF multiplicados de 1 a 9 e calcula-se o 
resto desta soma por 11. Se o resto for igual a 10, então o dígito é 0. Cálculo do 2º 
dígito: Soma os 9 primeiros números do CPF multiplicados de 9 a 1 e calcula-se o resto 
desta soma por 11. Se o resto for igual a 10, então o dígito é 0. Após  o  cálculo,  
compara-se  com  as  respectivas  posições  da  string  e  informe  se  o  CPF  é  
válido  ou inválido.
'''
cpf = ""
d1 = 0
d2 = 0
while True:
    cpf = input("Digite somente os numeros do seu CPF: ")
    if not cpf.isdigit() or len(cpf) > 11: print("CPF invalido")
    else: break

for i,d in enumerate(cpf[:9]):
    d1 += int(d) * (i+1)
    d2 += int(d) * (9-i)
    
d1 = 0 if d1%11 == 10 else d1%11
d2 = 0 if d2%11 == 10 else d2%11
if str(d1)+str(d2) == cpf[9:]: print("CPF Valido!")
else: print("CPF Invalido!")

