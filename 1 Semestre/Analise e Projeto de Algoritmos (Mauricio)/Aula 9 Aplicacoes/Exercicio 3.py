'''3) Elabore um algoritmo para calcular e mostrar a soma:
S = 2 + 2^2 + 2^3 + 2^4 + 2^5 + ... + 2^10  '''

soma = 0
for i in range(1,11): soma += 2**i
print(f"O valor da soma e {soma}")
