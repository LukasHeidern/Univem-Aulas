def gauss_t(matrix):
    for p in range(len(matrix)-1):
        for l in range(1+p,len(matrix)):
            if matrix[p][p] != 0:
                p_m = matrix[l][p] / matrix[p][p]
                for c in range(len(matrix[l])):
                    matrix[l][c] = matrix[l][c] - p_m * matrix[p][c]
    return matrix

def main():
    