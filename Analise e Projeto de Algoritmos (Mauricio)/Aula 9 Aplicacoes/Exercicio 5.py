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
