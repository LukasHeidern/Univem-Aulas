from random import sample

def menor_linha(l):
    a = matriz[l][0]
    for i in range(10):
        if matriz[l][i] < a:
            a = matriz[l][i]
    return a


def maior_coluna(c):
    b = matriz[0][c]
    for i in range(10):
        if matriz[i][c] < b:
            b = matriz[i][c]
    return b


print("Matriz:")
matriz = []
for i in range(10):
    matriz.append(sample(range(51),10))
    print(f"{matriz[i]:2}")




