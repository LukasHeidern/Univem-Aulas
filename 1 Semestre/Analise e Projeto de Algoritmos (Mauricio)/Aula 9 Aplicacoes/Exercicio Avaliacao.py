from random import randint

wA = 0
wB = 0
wC = 0

while True:
    A = randint(1, 2)  #int(input("\nDigite 2 ou 1: "))
    B = randint(1, 2)  #int(input("\nDigite 2 ou 1: "))
    C = int(input("\nDigite 2 ou 1: "))

    if A != B == C:
        print("\nO jogador A ganhou!")
        wA += 1
        if wA == 3:
            print("O jogador A eh o grande vecedor!!!")
            break
    elif C != B == A:
        print("\nVoce ganhou!")
        wC += 1
        if wC == 3:
            print("Voce eh o grande vecedor!!!")
            break
    elif B != A == C:
        print("\nO jogador B ganhou!")
        wB += 1
        if wB == 3:
            print("O jogador B eh o grande vecedor!!!")
            break
    else:
        print("Empate!")
