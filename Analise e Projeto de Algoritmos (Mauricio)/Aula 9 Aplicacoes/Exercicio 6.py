
a = 1
atleta = 0
t = 0
t_menor = 10

while a <= 10:
    t = float(input(f"Digite o tempo do atleta {a}"))
    if t < 1 and t > 10:
        print("Tempo Invalido")

    else:
        a += 1
        if t < t_menor:
            t_menor = t
            atleta = a


print(f"Menor Tempo {t_maior} - atleta {a}")