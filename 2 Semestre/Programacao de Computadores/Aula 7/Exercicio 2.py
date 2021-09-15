from random import sample

def verify(v,n):
    if len(v) == 0: return False
    elif n == v[0]: return True
    return verify(v[1:],n)

v = sample(range(0,101),10)
print(v)
n = int(input("Digite o valor que deseja verificar: "))
if verify(v,n): print("True")
else: print("False")



