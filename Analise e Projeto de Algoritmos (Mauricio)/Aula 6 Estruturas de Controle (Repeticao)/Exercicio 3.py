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

while True:
    sn = 0
    med = 0

    med_geral = 0

    rp = 0
    ap = 0

    i = 1

    while i <= 5:

        n1 = float(input("Digite a primeira nota: "))
        n2 = float(input("Digite a segunda nota: "))

        if (0 <= n1 <= 10) and (0 <= n2 <= 10):
            med = (n1 + n2) / 2

            if med < 6:
                print(f"Reprovado com media {med}\n")
                rp += 1

            else:
                print(f"Aprovado com media {med}\n")
                ap += 1

            i += 1
            med_geral += med

        else:
            print("Valores Invalidos!\n")
            break

    med_geral = med_geral / 5
    print(f"Media Geral - {med_geral}\nAprovados - {ap}\nReprovados - {rp}")

    while sn != 'N' and sn != 'S':
        sn = input("Deseja tentar novamente [S/N]: ").upper()[0]

    if sn == 'N':
         break

