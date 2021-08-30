from random import choice
## valida a senha passada por argumento

def validate(pword):
    L_upper = False
    S_char = False
    N_umber = False
    if len(pword) >= 8:
        for c in pword:
            if c.isspace(): return False
            elif c.isupper(): L_upper = True
            elif c.isdigit(): N_umber  = True
            elif not c.isdigit() and not c.isalpha(): S_char = True
    else: return False

    if L_upper and S_char and N_umber: return True
    return False

def sugestions(pword):
    if not pword[0].isdigit() and pword[0].isalpha():
        pword.insert(choice(['#','$','%','&','!','@'],0))
        print(pword)

senha = input("Digite uma senha:")
sugestions(senha)