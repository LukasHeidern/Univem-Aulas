# def solution(matrix):


def gauss_t(matrix):
    for p in range(len(matrix) - 1):
        for l in range(1 + p, len(matrix)):
            if matrix[p][p] != 0:
                p_m = matrix[l][p] / matrix[p][p]
                for c in range(len(matrix[l])):
                    matrix[l][c] = matrix[l][c] - p_m * matrix[p][c]
    return matrix


matrix = []
for i in range(int(input("quantas variaveis diferentes possuem os sistemas?: "))):
    matrix.append(list(map(float, input("Digite os coeficientes separados por espaco: ").split())))
for i in gauss_t(matrix): print(*i)