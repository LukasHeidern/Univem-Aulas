from functools import reduce
from operator import add

def soma_nat(n):
    return reduce(add,[i for i in range(1,n+1)])

N = int(input("Digite o valor: "))
print(f"a soma de todos os numeros e {soma_nat(N)}")