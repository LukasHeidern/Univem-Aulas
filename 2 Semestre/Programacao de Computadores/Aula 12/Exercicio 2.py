from random import randint

jogadas  = {}

for i in range(100):

    jogada = randint(1,6)

    if jogada in jogadas.keys(): jogadas[jogada] += 1
    else: jogadas[jogada] = 1

print(list(sorted(jogadas.items())))
