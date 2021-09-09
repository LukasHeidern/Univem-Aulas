
def gauss(matrix):
    for p in range(len(matrix)-1):
        for l in range(1+p,len(matrix)):
            if matrix[p][p] != 0:
                p_m = matrix[p+1][p] / matrix[p][p]
                for c in range(len(matrix[l])):
                    matrix[l][c] = matrix[l][c] - p_m * matrix[p][c]
    return matrix

matrix = []
for i in range(int(input("Tamanho da matriz: "))):
    matrix.append(list(map(float,input(f"Digite os elementos da linha {i+1} separados por espaco: ").split())))

for i in gauss(matrix): print(*i)