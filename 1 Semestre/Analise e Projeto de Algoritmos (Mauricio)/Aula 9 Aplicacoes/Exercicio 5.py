'''5) Um colégio quer certificar com honra ao mérito o aluno que obteve a melhor 
média final entre todos. Considerando que a turma possui 40 aluno, elabore um 
algoritmo que leia o nome e a média final de cada aluno e, em seguida,  mostre  o 
nome e a média do melhor aluno (a maior entre todas).'''

from random import randint

i = 0 
n = 0
media = 0
aluno = 0

while n != 40: 
    i = float(input(f"media:"))
    if 0 <= i <= 10:
        n += 1
        if i > media:
            media = i; aluno = n
        print(f"Aluno {n} Media {i}")
    else: print("Media Invalida!")

print(f"O aluno {aluno} possui a maior media: {media}")

###############################################################################3

a = 1
m_media = 0
m_aluno = 0
media = 0

while a <= 5:
    aluno = input(f"Digite o nome do {a} aluno(a): ")
    media = float(input(f"Digite a media do(a) {aluno}"))
    if media >= 0 or media <= 10:
        a += 1
        if media > m_media:
            m_aluno = aluno
            m_media = media
    else:
        print("numero invalido")
print(f"Melhor aluno(a) - {m_aluno}\nMaior media - {m_media}")
