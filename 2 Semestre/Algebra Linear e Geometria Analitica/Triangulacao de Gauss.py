### Lucas Ferrari Lopes - 617571
def gauss_s(matrix):
    m = matrix
    aux = 0
    s = [0] * len(matrix)
    for i in range(len(matrix) - 1, -1, -1):
        aux = 0
        for j in range(0, len(m[i]) - 1):
            if j != i: aux += m[i][j] * s[j]
        s[i] = (m[i][-1] - aux) / m[i][i]
    return s

def gauss_t(matrix):
    for p in range(len(matrix) - 1):
        for l in range(1 + p, len(matrix)):
            if matrix[p][p] != 0:
                p_m = matrix[l][p] / matrix[p][p]
                for c in range(len(matrix[l])):
                    matrix[l][c] = matrix[l][c] - p_m * matrix[p][c]
    return matrix

def g_matrix(n):
    matrix = []
    for i in range(n):matrix.append(list(map(float, input("Digite os coeficientes separados por espaco: ").split())))
    return matrix


def main():
    n = int(input("Quantas variaveis diferentes o sistema possui: "))
    matriz = g_matrix(n)

    for i in matriz:
        for j in i: print(f"{j:5}", end="")
        print()
    print()

    matriz_s = gauss_t(matriz)

    for x in matriz_s:
        for y in x: print(f"{y:5}", end="")
        print()
    print()

    solution = gauss_s(matriz)

    for i in range(len(solution)):
        print(f"x{i + 1} = {solution[i]}")


main()