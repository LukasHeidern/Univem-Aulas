def comb(n,k):
    if k == 1: return n
    elif k == n: return 1
    return comb(n-1, k-1) + comb(n-1, k)

n = int(input("Quantas pessoas no total?: "))
k = int(input("Quantas pessoas por grupo?: "))
print(comb(n,k))