########################## CODE DUMP #######################################################################################
'''
3) Considerando uma classe com 60 alunos,
elabore um algoritmo que leia duas notas de
cada aluno, calcule a media e verifique se o
aluno foi aprovado ou reprovado.
Para estar aprovado a media devera ser maior
ou igual a 6. Determine a media geral da classe
e a quantidade de alunos aprovados e reprovados
da turma.
'''

med = 0
med_geral = 0

yn = False

rp = 0
ap = 0

i = 1
while True:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))

    if  0 < n1 < 10 and 0 < n2 < 10:
        while i <= 5:
            med = (n1 + n2) / 2
            if med < 6:
                print(f"Reprovado com media {med}\n")
                rp += 1
            else:
                print(f"Aprovado com media {med}\n")
                ap += 1
            i += 1
            med_geral += med
        med_geral = med_geral / 5
        print(f"Media Geral - {med_geral}\nAprovados - {ap}\nReprovados - {rp}")
    else:
        while yn != 'S' or yn != 'N':
            yn = input("Valores Invalidos\nDeseja tentar novamente [S/N]: ").upper()[0]
            if yn == 'N':
                yn = 0
                break
            elif yn != 'S':
                print("Resposta invalida")



############################################################################################################################


med = 0
med_geral = 0
yn = True
rp = 0
ap = 0

i = 1

while True:  ### loop geral do programa
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))

    if 0 < n1 < 10 and 0 < n2 < 10:
        while i <= 5:  ### loop do calculo da media do aluno e se foi aprovado ou nao
            med = (n1 + n2) / 2
            if med < 6:
                print(f"Reprovado com media {med}\n")
                rp += 1
            else:
                print(f"Aprovado com media {med}\n")
                ap += 1
            i += 1
            med_geral += med
        med_geral = med_geral / 5
        print(f"Media Geral - {med_geral}\nAprovados - {ap}\nReprovados - {rp}")

    else:
        while yn:
            yn = input("Valores Invalidos\nDeseja tentar novamente [S/N]: ").upper()[0]
            if yn == 'S':
                yn = False


###############################################################################################################################



med = 0
med_geral = 0

loop = True
aux = 0

rp = 0
ap = 0

i = 1
while loop:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    loop = 0
    if  0 < n1 < 10 and 0 < n2 < 10:
        while i <= 5:
            med = (n1 + n2) / 2
            if med < 6:
                print(f"Reprovado com media {med}\n")
                rp += 1
            else:
                print(f"Aprovado com media {med}\n")
                ap += 1
            i += 1
            med_geral += med
        med_geral = med_geral / 5
        print(f"Media Geral - {med_geral}\nAprovados - {ap}\nReprovados - {rp}")

    else:
        while aux != 'N' or loop != 'S':
            aux = input("Valores Invalidos\nDeseja tentar novamente [S/N]: ").upper()[0]

            if aux == 'N':
                loop = False


#######################################################################################################################
####################CORRETO##################################################################################

med = 0
med_geral = 0

rp = 0
ap = 0

i = 1
while True:

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))

    sn = 0

    if (0 < n1 < 10) and (0 < n2 < 10):
        while i <= 5:
            med = (n1 + n2) / 2
            if med < 6:
                print(f"Reprovado com media {med}\n")
                rp += 1
            else:
                print(f"Aprovado com media {med}\n")
                ap += 1
            i += 1
            med_geral += med
        med_geral = med_geral / 5
        print(f"Media Geral - {med_geral}\nAprovados - {ap}\nReprovados - {rp}")

        while sn != 'N' and sn != 'S':
            sn = input("Valores Invalidos\nDeseja tentar novamente [S/N]: ").upper()[0]
    else:
        if sn == 'N':
            break
