from functools import reduce
from operator import mul
from random import sample

def prod_lista(lista):
    return reduce(mul,lista)

lista1 = sample(range(1,11),5)
print(f"Produto dos elementos: {prod_lista(lista1)}")
