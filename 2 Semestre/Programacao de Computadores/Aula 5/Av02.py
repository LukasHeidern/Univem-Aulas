from random import randint,choice,sample

### Valida a senha passada por argumento
def validate(P_word):
    L_upper = False
    S_char = False
    N_umber = False
    if len(P_word) >= 8:
        for c in P_word:
            if c.isspace(): return False
            elif c.isupper(): L_upper = True
            elif c.isdigit(): N_umber  = True
            elif not c.isdigit() and not c.isalpha(): S_char = True
    else: return False
    if L_upper and S_char and N_umber: return True
    return False

### Gera sugestoes de senhas para o usuario
def sugestions(P_word):
    P_sugestions = []
    for i in range(3):
        pw = list(''.join(P_word.split()))
        pw.insert(choice([0,len(pw)]), ['_','*', '#', '$', '%', '&', '!', '@'][randint(0, 7)])
        pw.insert(choice([0, len(pw)]), str(randint(0, 9)))
        if len(pw) < 8: pw.extend(map(str,sample(range(0,9),8-len(pw))))
        for i,j in enumerate(pw):
            if j.isalpha(): pw[i] = j.upper(); break
        P_sugestions.append(''.join(pw))
    return P_sugestions

### funcao principal
def main():
    print("Para cadastrar devidamente sua senha ela deve possuir:"
          "\n1 caractere especial;"
          "\n1 numero e;"
          "\n1 letra maiuscula.")
    senha = input("Digite a senha: ")
    if validate(senha):
        print("Senha Valida!")
    else:
        print("Senha Invalida! Tente algo como: ")
        for i in sugestions(senha):
            print(i)

main()