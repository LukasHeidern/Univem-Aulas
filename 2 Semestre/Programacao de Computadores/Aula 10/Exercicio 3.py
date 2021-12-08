from random import sample

def indices_pares(lista):
    return [lista[i] for i in range(0,len(lista),2)]

lista = sample(range(50),10)

print(f"Lista: {lista}")
print(f"Lista indices pares: {indices_pares(lista)}")
