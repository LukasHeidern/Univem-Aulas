'''7.) Elabore um algoritmo que mostre todos os números ascendentes menores que 1000. 
Um número é ascendente se seus algarismos estão em ordem crescente. Por exemplo, o 
número 258 é ascendente, pois, 2 < 5 e 5 < 8.'''

for i in range(1,1000):
    u = i % 10
    d = i % 100 //10
    c = i // 100

    if c > d > u: print(i)
    