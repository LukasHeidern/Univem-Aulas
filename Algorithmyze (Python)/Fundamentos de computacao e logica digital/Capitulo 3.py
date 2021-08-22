
def notacao_posicional():
### NOTACAO POSICIONAL

    '''numeros na base 'b' possuem digitos que representam valores que vao de zero (0) a 'b-1'
    focando no objetivo que sao as bases 2, 4, 8, 10 e 16 os algarismos delas seriam os seguintes:

        Algebricamente pode ser representado da seguinte maneira:

        (numeros que representam a parte positiva)
        ... (N[-p] * B ^ (-p)) + (N[-2] * B ^ (-2)) + (N[-1] * B ^ (-1))

        (numeros que representam a parte negativa)
        (N[0] * B ^ (0)) + (N[1] * B ^ (1)) + (N[p] * B ^ (p)) ...

        onde:
        'N' e o valor passado;
        'B' e a base;
        'p' e a posicao do algarismo
    '''

    while True:
        base = int(input("Exibir algarismos da"
                         "\nBase 2 (Base Binaria)"
                         "\nBase 4 (... ¯\_(ツ)_/¯)"
                         "\nBase 8 (Base Octal)"
                         "\nBase 10 (Base Decimal)"
                         "\nBase 16 (Base Hexadecimal)"
                         ">>> "))
        if base not in [2, 4, 8, 10, 16]: print("Base Invalida!!!(╬ ಠ益ಠ)")
        else: break

    algarismos = []
    for p in range(0,base):
        if base <= 10 and p > 9: algarismos.append(['A','B','C','D','E','F'][p-9])
        else: algarismos.append(p)
    print(f" っ▀¯▀)つ Os algarismos da base {base} sao: ",*algarismos)
    return algarismos

##########################################################################################

def dados_numericos():
### REPRESENTACAO DE DADOS NUMERICOS NAS BASES 2,4,8,10 E 16

    '''Uma grandeza qualquer pode ser representada por uma sequencia de digitos numericos quaisquer
    de uma determinada base'''

    '''Na Base Hexadecimal (16) os valores 10, 11, 12, 13, 14 e 15 sao representados por
    'A' 'B' 'C' 'D' 'E' e 'F' respectivamente'''

    while True:
        base = int(input("Representar algarismos da"
                         "\nBase 2 (Base Binaria)"
                         "\nBase 4 (... ¯\_(ツ)_/¯)"
                         "\nBase 8 (Base Octal)"
                         "\nBase 10 (Base Decimal)"
                         "\nBase 16 (Base Hexadecimal)"
                         ">>> "))
        if base not in [2, 4, 8, 10, 16]: print("Base Invalida!!!(╬ ಠ益ಠ)")
        else: break

    if base == 2:
        valor = int(input(f"Digite um valor em binario: "))
        print("A equacao e: ",valor)
        for i,j in enumerate(str(valor).split()):
            print(f"{valor[i]}[{j}] * {base} ^ ({j}))")
