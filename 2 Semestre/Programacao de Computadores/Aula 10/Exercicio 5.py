
def media_digitos(n):
    num = list(map(int,str(n)))
    return sum(num) / len(num)

n = int(input("digite o valor: "))
print(f"a media dos valores e: {media_digitos(n)}")