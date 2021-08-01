'''7) Elabore um algoritmo que determine se um ano é ou não bissexto. 
Obs. Um ano é bissexto se ele for divisível por 400 ou se ele for divisível por 4 e 
não por 100.'''

ano = int(input("Digite o ano: "))

if (ano % 400 == 0) or ((ano % 4  == 0) and (ano % 100 != 0)): print(f"{ano} e um Ano Bissexto")
else: print(f"{ano} nao e um Ano Bissexto")