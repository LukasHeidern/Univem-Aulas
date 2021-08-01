



for num in range(1,10000):
    soma = 0
    for d in range(1, num//2+1):
        if num % d == 0:
            soma += d
    if soma == num:
        print(num)