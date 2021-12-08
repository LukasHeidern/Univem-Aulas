def quadrado(n):
    return [i**2 for i in range(2,n+1)]

N = int(input("Digite o valor: "))
print(f"quadrados perfeitos de 2 a {N}: {quadrado(N)}")